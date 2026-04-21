"""
visualizer.py — CNN 아키텍처 시각화 + 교육적 상세 뷰

상단: 3D 투시도로 feature map 스택이 겹쳐진 CNN 아키텍처 전체 그림
하단: 각 레이어의 동작 원리를 교육적으로 시각화
  - Conv: 입력 + 3×3 커널 가중치 + 출력 feature map
  - Pool: 풀링 전후 비교 (크기 변화)
  - FC: Pool2 → Flatten(784) → FC(64) 변환 과정
  - Output: 숫자별 확률 바 차트

모든 데이터는 실제 모델의 forward pass 결과입니다.
"""

import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.gridspec as gridspec

plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

LAYERS = [
    {'name': 'Input',  'size': '28×28×1',  'color': '#4A90D9', 'n_cards': 1,  'card_h': 1.0,
     'desc': '입력: 손글씨 이미지 28×28'},
    {'name': 'Conv1',  'size': '28×28×8',  'color': '#E8734A', 'n_cards': 6,  'card_h': 1.0,
     'desc': 'Conv1: 3×3 필터 8개로 합성곱 → 에지/선 감지'},
    {'name': 'Pool1',  'size': '14×14×8',  'color': '#F5A623', 'n_cards': 6,  'card_h': 0.7,
     'desc': 'Pool1: 2×2 맥스풀링 → 크기 절반으로 축소'},
    {'name': 'Conv2',  'size': '14×14×16', 'color': '#E8734A', 'n_cards': 8,  'card_h': 0.7,
     'desc': 'Conv2: 3×3 필터 16개로 합성곱 → 곡선/형태 감지'},
    {'name': 'Pool2',  'size': '7×7×16',   'color': '#F5A623', 'n_cards': 8,  'card_h': 0.45,
     'desc': 'Pool2: 2×2 맥스풀링 → 7×7로 압축'},
    {'name': 'Flatten\n+FC', 'size': '784→64', 'color': '#7ED321', 'n_cards': 1,  'card_h': 1.2,
     'desc': 'Flatten + FC: 2D→1D 변환 후 64개 뉴런으로 조합'},
    {'name': 'Output', 'size': '10',       'color': '#D0021B', 'n_cards': 1,  'card_h': 1.2,
     'desc': 'Output: 소프트맥스 → 숫자별 확률'},
]
ACT_KEYS = [None, 'relu1', 'pool1', 'relu2', 'pool2', 'fc1', 'fc2']


class CNNVisualizer:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.activations = None
        self.input_image = None
        self.probabilities = None
        self.predicted = None
        self.weights = None
        self.current_frame = -1
        self._timer_id = None
        self._layer_hitboxes = []
        self._arch_ax = None

        self.fig = Figure(figsize=(13, 8), facecolor='white', dpi=100)
        self.canvas_widget = FigureCanvasTkAgg(self.fig, master=parent_frame)
        self.tk_widget = self.canvas_widget.get_tk_widget()
        self.tk_widget.pack(fill='both', expand=True)
        self.fig.canvas.mpl_connect('button_press_event', self._on_click)
        self._show_welcome()

    def _show_welcome(self):
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.set_facecolor('white')
        ax.text(0.5, 0.55, 'CNN 시각화', fontsize=28, color='#222222',
                ha='center', va='center', fontweight='bold')
        ax.text(0.5, 0.40, '왼쪽 캔버스에 숫자를 그려주세요',
                fontsize=14, color='#999999', ha='center', va='center')
        ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis('off')
        self.canvas_widget.draw()

    # ====== 애니메이션 제어 ======
    def visualize(self, activations, input_image, predicted, probabilities, weights=None):
        self.activations = activations
        self.input_image = input_image
        self.predicted = predicted
        self.probabilities = probabilities
        self.weights = weights
        self._cancel_timer()
        self.current_frame = 0
        self._draw(0)
        self.current_frame = 1

    def _cancel_timer(self):
        if self._timer_id is not None:
            self.tk_widget.after_cancel(self._timer_id)
            self._timer_id = None

    def _auto_play_tick(self):
        if self.current_frame > 6:
            self._timer_id = None; return
        self._draw(self.current_frame)
        self.current_frame += 1
        self._timer_id = self.tk_widget.after(800, self._auto_play_tick)

    def step_forward(self):
        if self.activations is None: return
        self._cancel_timer()
        if self.current_frame <= 6:
            self._draw(self.current_frame)
            self.current_frame += 1

    def auto_play(self):
        if self.activations is None: return
        self._cancel_timer(); self._auto_play_tick()

    def replay(self):
        if self.activations is not None:
            self.current_frame = 0; self._cancel_timer(); self._auto_play_tick()

    def jump_to(self, idx):
        if self.activations is None or idx < 0 or idx > 6: return
        self._cancel_timer(); self._draw(idx); self.current_frame = idx + 1

    def _on_click(self, event):
        if self.activations is None or event.inaxes is None: return
        if event.inaxes != self._arch_ax or event.xdata is None: return
        for i, (xmin, xmax) in enumerate(self._layer_hitboxes):
            if xmin <= event.xdata <= xmax:
                self.jump_to(i); return

    # ====== 메인 렌더링 ======
    def _draw(self, frame_num):
        self.fig.clear()
        gs = gridspec.GridSpec(2, 1, figure=self.fig, height_ratios=[2, 3], hspace=0.08)

        ax_arch = self.fig.add_subplot(gs[0])
        self._arch_ax = ax_arch
        self._draw_architecture(ax_arch, frame_num)

        if frame_num == 0:
            self._draw_detail_input(gs[1])
        elif frame_num in (1, 3):
            self._draw_detail_conv(gs[1], frame_num)
        elif frame_num in (2, 4):
            self._draw_detail_pool(gs[1], frame_num)
        elif frame_num == 5:
            self._draw_detail_flatten_fc(gs[1])
        else:
            self._draw_detail_output(gs[1])

        self.fig.set_facecolor('white')
        self.canvas_widget.draw()

    # ====== 상단: 3D 아키텍처 ======
    def _draw_architecture(self, ax, active_idx):
        ax.set_xlim(-2, 105); ax.set_ylim(-4, 12)
        ax.set_facecolor('white'); ax.axis('off')

        layer_x = [0, 14, 28, 42, 58, 74, 90]
        self._layer_hitboxes = []

        for i, (lx, layer) in enumerate(zip(layer_x, LAYERS)):
            is_active = (i == active_idx)
            is_past = (i < active_idx)
            n_cards = layer['n_cards']
            card_h = layer['card_h'] * 7
            card_w = card_h * 0.75
            stack_offset = 0.35
            total_w = card_w + (n_cards - 1) * stack_offset
            self._layer_hitboxes.append((lx - 1, lx + total_w + 1))
            alpha_base = 1.0 if is_active else (0.55 if is_past else 0.3)
            fmaps = self._get_layer_images(i)

            for c in range(n_cards - 1, -1, -1):
                cx = lx + c * stack_offset
                cy = -card_h / 2 + 4 + c * stack_offset
                alpha = alpha_base * (0.6 + 0.4 * (c / max(n_cards - 1, 1)))
                rect = plt.Rectangle((cx, cy), card_w, card_h,
                    facecolor='white', edgecolor=layer['color'],
                    linewidth=2.0 if (is_active and c == n_cards - 1) else 0.8,
                    alpha=alpha, zorder=10 + c)
                ax.add_patch(rect)
                if fmaps is not None and c < len(fmaps):
                    ax.imshow(fmaps[c], cmap='Blues' if i > 0 else 'gray',
                              extent=[cx+0.15, cx+card_w-0.15, cy+0.15, cy+card_h-0.15],
                              aspect='auto', alpha=alpha*0.9, zorder=11+c,
                              interpolation='bilinear', vmin=0, vmax=1)

            if is_active:
                bar_y = -card_h / 2 + 4 - 0.8
                ax.plot([lx, lx+total_w], [bar_y, bar_y],
                        color=layer['color'], linewidth=3, zorder=30, solid_capstyle='round')

            label_y = -card_h / 2 + 4 - 1.5
            nc = layer['color'] if is_active else ('#666666' if is_past else '#CCCCCC')
            ax.text(lx+total_w/2, label_y, layer['name'], fontsize=9, color=nc,
                    ha='center', va='top', fontweight='bold' if is_active else 'normal', zorder=30)
            ax.text(lx+total_w/2, label_y-1.2, layer['size'], fontsize=7, color=nc,
                    ha='center', va='top', alpha=0.7, zorder=30)

            if i > 0:
                prev_total = LAYERS[i-1]['card_h']*7*0.75 + (LAYERS[i-1]['n_cards']-1)*stack_offset
                s = layer_x[i-1] + prev_total + 0.5
                e = lx - 0.5
                ac = LAYERS[i]['color'] if i <= active_idx else '#DDDDDD'
                aa = 0.7 if i <= active_idx else 0.3
                ax.annotate('', xy=(e, 4), xytext=(s, 4),
                            arrowprops=dict(arrowstyle='->', color=ac, lw=1.5, alpha=aa), zorder=5)

        ax.text(52, 11, LAYERS[active_idx]['desc'], fontsize=11, color='#333333',
                ha='center', va='center', fontweight='bold')

    def _get_layer_images(self, layer_idx):
        if layer_idx == 0:
            img = self.input_image
            if img is not None:
                mn, mx = img.min(), img.max()
                if mx > mn: img = (img - mn) / (mx - mn)
                return [img]
            return None
        act_key = ACT_KEYS[layer_idx]
        if act_key is None or self.activations is None or act_key not in self.activations:
            return None
        if layer_idx <= 4:
            maps = self.activations[act_key].squeeze(0).numpy()
            n = min(maps.shape[0], LAYERS[layer_idx]['n_cards'])
            result = []
            for i in range(n):
                fm = maps[i]; fn, fx = fm.min(), fm.max()
                if fx > fn: fm = (fm - fn) / (fx - fn)
                else: fm = np.zeros_like(fm)
                result.append(fm)
            return result
        vals = self.activations[act_key].squeeze().numpy()
        vmax = max(abs(vals.max()), abs(vals.min()), 1e-6)
        normalized = (vals / vmax + 1) / 2
        side = int(np.ceil(np.sqrt(len(normalized))))
        padded = np.zeros(side * side)
        padded[:len(normalized)] = normalized
        return [padded.reshape(side, side)]

    # ====== 하단: 입력 이미지 ======
    def _draw_detail_input(self, parent_gs):
        gs = parent_gs.subgridspec(1, 2, width_ratios=[1, 2], wspace=0.3)
        ax = self.fig.add_subplot(gs[0])
        ax.imshow(self.input_image, cmap='gray', interpolation='nearest')
        ax.set_title('전처리된 입력 (28×28)', fontsize=11, color='#333333', pad=8)
        ax.axis('off')

        ax2 = self.fig.add_subplot(gs[1])
        ax2.set_facecolor('white'); ax2.axis('off')
        ax2.set_xlim(0, 1); ax2.set_ylim(0, 1)
        ax2.text(0.05, 0.85,
            "입력 데이터\n\n"
            "• 손으로 그린 숫자를 28×28 픽셀로 변환\n"
            "• 숫자를 이미지 중앙에 정렬\n"
            "• MNIST 데이터셋과 동일하게 정규화\n"
            "• 1개 채널 (흑백) 이미지\n\n"
            "→ 이 이미지가 Conv1의 입력이 됩니다",
            fontsize=10, color='#444444', va='top', linespacing=1.6)

    # ====== 하단: Conv 레이어 (입력 + 커널 + 출력) ======
    def _draw_detail_conv(self, parent_gs, frame_num):
        layer = LAYERS[frame_num]
        act_key = ACT_KEYS[frame_num]
        maps = self.activations[act_key].squeeze(0).numpy()
        n_maps = maps.shape[0]

        # 커널 가중치
        w_key = 'conv1' if frame_num == 1 else 'conv2'
        kernels = self.weights[w_key] if self.weights else None  # (out, in, 3, 3)

        # 입력 이미지
        if frame_num == 1:
            input_img = self.input_image
        else:
            input_img = self.activations['pool1'].squeeze(0).numpy()[0]
            mn, mx = input_img.min(), input_img.max()
            if mx > mn: input_img = (input_img - mn) / (mx - mn)

        # 레이아웃: 제목 + [입력 | 커널들 | 출력 feature maps]
        gs = parent_gs.subgridspec(2, 3, height_ratios=[0.3, 1],
                                    width_ratios=[1, 1.2, 2], wspace=0.25, hspace=0.2)

        # 제목
        ax_title = self.fig.add_subplot(gs[0, :])
        ax_title.axis('off')
        ax_title.text(0.0, 0.2,
            f'{layer["name"]}  —  입력에 3×3 필터를 슬라이딩하며 합성곱 연산',
            fontsize=12, color=layer['color'], fontweight='bold', va='center')

        # 왼쪽: 입력 이미지
        ax_in = self.fig.add_subplot(gs[1, 0])
        ax_in.imshow(input_img, cmap='gray', interpolation='nearest')
        h, w = input_img.shape[:2]
        ax_in.set_title(f'입력 ({h}×{w})', fontsize=10, color='#333333', pad=5)
        # 3×3 커널 위치 표시 (좌상단에 빨간 사각형)
        rect = plt.Rectangle((0, 0), 3, 3, linewidth=2, edgecolor='red',
                              facecolor='none', zorder=10)
        ax_in.add_patch(rect)
        ax_in.text(1.5, -1.5, '3×3 영역', fontsize=7, color='red', ha='center')
        ax_in.axis('off')

        # 중간: 커널(필터) 가중치 그리드
        ax_kern = self.fig.add_subplot(gs[1, 1])
        ax_kern.set_facecolor('white'); ax_kern.axis('off')
        if kernels is not None:
            # 첫 입력 채널의 커널 4개만 표시 (2×2 그리드)
            show_k = min(n_maps, 4)
            k_rows, k_cols = 2, 2
            kh, kw = kernels.shape[2], kernels.shape[3]
            grid = np.ones((k_rows * (kh+1) - 1, k_cols * (kw+1) - 1)) * 0.5
            for ki in range(show_k):
                r, c = ki // k_cols, ki % k_cols
                kern = kernels[ki, 0]  # 첫 번째 입력 채널
                kn, kx = kern.min(), kern.max()
                if kx > kn: kern = (kern - kn) / (kx - kn)
                y = r * (kh + 1)
                x = c * (kw + 1)
                grid[y:y+kh, x:x+kw] = kern
            ax_kern.imshow(grid, cmap='RdBu_r', interpolation='nearest', vmin=0, vmax=1)
            ax_kern.set_title(f'3×3 커널 (필터 1~{show_k})', fontsize=9, color='#666666', pad=5)

            # 연산 설명
            ax_kern.text(0.5, -0.15,
                '각 위치에서\n커널 × 입력 → 합산',
                fontsize=8, color='#888888', ha='center', va='top',
                transform=ax_kern.transAxes)

        # 오른쪽: 출력 feature map 그리드
        cols = 4 if n_maps <= 8 else 4
        rows = 2 if n_maps <= 8 else 4
        gs_out = gs[1, 2].subgridspec(rows, cols, hspace=0.3, wspace=0.2)
        show = min(n_maps, rows * cols)
        for idx in range(show):
            r, c = idx // cols, idx % cols
            ax = self.fig.add_subplot(gs_out[r, c])
            fm = maps[idx]; fn, fx = fm.min(), fm.max()
            if fx > fn: fm = (fm - fn) / (fx - fn)
            ax.imshow(fm, cmap='Blues', interpolation='nearest', vmin=0, vmax=1)
            ax.set_title(f'{idx+1}', fontsize=6, color='#666666', pad=1)
            ax.axis('off')
            for sp in ax.spines.values():
                sp.set_edgecolor(layer['color']); sp.set_linewidth(0.8); sp.set_visible(True)

    # ====== 하단: Pool 레이어 (전후 비교) ======
    def _draw_detail_pool(self, parent_gs, frame_num):
        layer = LAYERS[frame_num]
        act_key = ACT_KEYS[frame_num]
        pool_maps = self.activations[act_key].squeeze(0).numpy()

        # 풀링 전 데이터 (conv 출력)
        prev_key = 'relu1' if frame_num == 2 else 'relu2'
        before_maps = self.activations[prev_key].squeeze(0).numpy()

        gs = parent_gs.subgridspec(2, 1, height_ratios=[0.3, 1], hspace=0.15)

        # 제목
        ax_title = self.fig.add_subplot(gs[0])
        ax_title.axis('off')
        bh, bw = before_maps.shape[1], before_maps.shape[2]
        ah, aw = pool_maps.shape[1], pool_maps.shape[2]
        ax_title.text(0.0, 0.2,
            f'{layer["name"]}  —  2×2 영역에서 최댓값 선택 → {bh}×{bw} → {ah}×{aw} (크기 절반)',
            fontsize=12, color=layer['color'], fontweight='bold', va='center')

        # 메인: 풀링 전 3개 + 화살표 + 풀링 후 3개 + 전체 그리드
        gs_main = gs[1].subgridspec(2, 7, height_ratios=[2, 1], wspace=0.15, hspace=0.3)

        # 상단: 풀링 전후 비교 (대표 3개 필터)
        for idx in range(3):
            # 풀링 전
            ax_b = self.fig.add_subplot(gs_main[0, idx])
            bm = before_maps[idx]; bn, bx = bm.min(), bm.max()
            if bx > bn: bm = (bm - bn) / (bx - bn)
            ax_b.imshow(bm, cmap='Blues', interpolation='nearest', vmin=0, vmax=1)
            ax_b.set_title(f'전 ({bh}×{bw})', fontsize=7, color='#E8734A', pad=2)
            ax_b.axis('off')

            # 화살표 영역
            if idx == 1:
                ax_arr = self.fig.add_subplot(gs_main[0, 3])
                ax_arr.axis('off')
                ax_arr.set_xlim(0, 1); ax_arr.set_ylim(0, 1)
                ax_arr.annotate('', xy=(0.9, 0.5), xytext=(0.1, 0.5),
                    arrowprops=dict(arrowstyle='->', color=layer['color'], lw=2.5))
                ax_arr.text(0.5, 0.3, 'Max\nPool\n2×2', fontsize=8,
                           color=layer['color'], ha='center', va='center', fontweight='bold')

            # 풀링 후
            ax_a = self.fig.add_subplot(gs_main[0, 4 + idx])
            pm = pool_maps[idx]; pn, px = pm.min(), pm.max()
            if px > pn: pm = (pm - pn) / (px - pn)
            ax_a.imshow(pm, cmap='Blues', interpolation='nearest', vmin=0, vmax=1)
            ax_a.set_title(f'후 ({ah}×{aw})', fontsize=7, color=layer['color'], pad=2)
            ax_a.axis('off')

        # 하단: 전체 feature map 그리드 (작게)
        n = pool_maps.shape[0]
        gs_grid = gs_main[1, :].subgridspec(1, min(n, 8), wspace=0.1)
        for idx in range(min(n, 8)):
            ax = self.fig.add_subplot(gs_grid[0, idx])
            fm = pool_maps[idx]; fn, fx = fm.min(), fm.max()
            if fx > fn: fm = (fm - fn) / (fx - fn)
            ax.imshow(fm, cmap='Blues', interpolation='nearest', vmin=0, vmax=1)
            ax.set_title(f'{idx+1}', fontsize=6, color='#999999', pad=1)
            ax.axis('off')

    # ====== 하단: Flatten + FC ======
    def _draw_detail_flatten_fc(self, parent_gs):
        pool2 = self.activations['pool2'].squeeze(0).numpy()  # (16, 7, 7)
        fc1 = self.activations['fc1'].squeeze().numpy()         # (64,)

        gs = parent_gs.subgridspec(2, 3, height_ratios=[0.25, 1],
                                    width_ratios=[1, 0.5, 1.5], wspace=0.2, hspace=0.15)

        # 제목
        ax_title = self.fig.add_subplot(gs[0, :])
        ax_title.axis('off')
        ax_title.text(0.0, 0.2,
            'Flatten + FC  —  7×7×16 = 784개를 1차원으로 펼친 뒤 → 64개 뉴런으로 조합',
            fontsize=12, color='#7ED321', fontweight='bold', va='center')

        # 왼쪽: Pool2의 16개 feature map (4×4 그리드)
        gs_pool = gs[1, 0].subgridspec(4, 4, hspace=0.15, wspace=0.1)
        for idx in range(16):
            r, c = idx // 4, idx % 4
            ax = self.fig.add_subplot(gs_pool[r, c])
            fm = pool2[idx]; fn, fx = fm.min(), fm.max()
            if fx > fn: fm = (fm - fn) / (fx - fn)
            ax.imshow(fm, cmap='Blues', interpolation='nearest', vmin=0, vmax=1)
            ax.axis('off')
            if idx == 0:
                ax.set_title('7×7', fontsize=6, color='#999999', pad=1)

        # 중간: Flatten 시각화 (784개를 세로 컬러바로)
        ax_flat = self.fig.add_subplot(gs[1, 1])
        flat_data = pool2.flatten()  # 784개
        # 정규화
        fmin, fmax = flat_data.min(), flat_data.max()
        if fmax > fmin: flat_norm = (flat_data - fmin) / (fmax - fmin)
        else: flat_norm = np.zeros_like(flat_data)
        # 세로 컬러바 (784×1을 28×28로 재배열하여 표시)
        flat_img = flat_norm.reshape(28, 28)
        ax_flat.imshow(flat_img, cmap='Blues', interpolation='nearest', aspect='auto')
        ax_flat.set_title('Flatten\n784개', fontsize=9, color='#666666', pad=5)
        ax_flat.set_ylabel('← 2D를 1D로 펼침', fontsize=7, color='#999999')
        ax_flat.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

        # 화살표 텍스트
        ax_flat.text(0.5, -0.08, '→ FC →', fontsize=10, color='#7ED321',
                     ha='center', va='top', transform=ax_flat.transAxes, fontweight='bold')

        # 오른쪽: FC 활성화 바 차트
        ax_fc = self.fig.add_subplot(gs[1, 2])
        colors = ['#4ECDC4' if v > 0 else '#FF6B6B' for v in fc1]
        ax_fc.bar(range(len(fc1)), fc1, color=colors, width=0.8)
        ax_fc.set_title(f'FC 활성화 (64개 뉴런, 활성: {int(np.sum(fc1>0))}개)',
                        fontsize=10, color='#7ED321', fontweight='bold', pad=5)
        ax_fc.set_xlabel('뉴런', fontsize=8, color='#888888')
        ax_fc.set_xlim(-1, 64)
        ax_fc.tick_params(colors='#AAAAAA', labelsize=6)
        ax_fc.spines['top'].set_visible(False); ax_fc.spines['right'].set_visible(False)
        ax_fc.spines['bottom'].set_color('#DDDDDD'); ax_fc.spines['left'].set_color('#DDDDDD')
        ax_fc.set_facecolor('white')

    # ====== 하단: 출력 ======
    def _draw_detail_output(self, parent_gs):
        gs = parent_gs.subgridspec(1, 2, width_ratios=[3, 1], wspace=0.2)
        probs = self.probabilities
        ax = self.fig.add_subplot(gs[0])
        colors = ['#2ECC71' if d == self.predicted else '#E0E0E0' for d in range(10)]
        bars = ax.barh(range(10), probs, color=colors, height=0.6, edgecolor='none')
        for d, (bar, p) in enumerate(zip(bars, probs)):
            if p > 0.01:
                ax.text(p + 0.015, d, f'{p:.1%}', va='center', ha='left', fontsize=10,
                        color='#222222' if d == self.predicted else '#AAAAAA',
                        fontweight='bold' if d == self.predicted else 'normal')
        ax.set_yticks(range(10))
        ax.set_yticklabels([str(d) for d in range(10)], fontsize=14, color='#333333')
        ax.set_xlim(0, 1.2)
        ax.set_title(f'예측: {self.predicted}  (확신도 {probs[self.predicted]:.1%})',
                     fontsize=14, color='#2ECC71', fontweight='bold', pad=10)
        ax.invert_yaxis()
        ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_color('#DDDDDD'); ax.spines['left'].set_color('#DDDDDD')
        ax.tick_params(axis='x', colors='#AAAAAA', labelsize=8)
        ax.set_xlabel('확률', fontsize=9, color='#666666')
        ax.set_facecolor('white')

        ax2 = self.fig.add_subplot(gs[1])
        ax2.axis('off'); ax2.set_xlim(0, 1); ax2.set_ylim(0, 1)
        top3 = np.argsort(probs)[::-1][:3]
        t3 = '\n'.join([f'  {d}: {probs[d]:.1%}' for d in top3])
        ax2.text(0.05, 0.85,
            f"출력층 (소프트맥스)\n\n• FC의 64개 값 → 10개 출력\n"
            f"• 소프트맥스로 확률 변환\n• 합계 = 100%\n\n상위 3개:\n{t3}",
            fontsize=9, color='#444444', va='top', linespacing=1.6)
