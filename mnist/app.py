"""
app.py — MNIST 숫자 인식 + CNN 시각화 메인 애플리케이션

실행 방법:
    1. 먼저 모델 학습: python train_model.py
    2. 앱 실행: python app.py
"""

import os
import sys
import tkinter as tk
from tkinter import messagebox

import torch

from model import SimpleCNN
from drawing_canvas import DrawingCanvas
from preprocessor import preprocess
from visualizer import CNNVisualizer

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'saved_model', 'mnist_cnn.pth')

# 디자인 상수
BG = '#FFFFFF'
FG = '#222222'
FG_SUB = '#888888'
ACCENT = '#4A90D9'
FONT = 'Apple SD Gothic Neo'


class MNISTApp:
    """MNIST 숫자 인식 + CNN 시각화 애플리케이션"""

    def __init__(self):
        self.model = self._load_model()

        self.root = tk.Tk()
        self.root.title('MNIST 숫자 인식 — CNN 시각화')
        self.root.configure(bg=BG)
        self.root.resizable(False, False)

        self._build_ui()

        self.root.bind('<Escape>', lambda e: self.root.destroy())
        self.root.bind('<BackSpace>', lambda e: self._on_clear())
        self.root.bind('<space>', lambda e: self._on_step())

    def _load_model(self):
        if not os.path.exists(MODEL_PATH):
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror(
                '모델 파일 없음',
                f'학습된 모델을 찾을 수 없습니다.\n\n'
                f'먼저 다음 명령어로 모델을 학습해주세요:\n\n'
                f'  python train_model.py\n\n'
                f'찾는 경로: {MODEL_PATH}'
            )
            sys.exit(1)

        model = SimpleCNN()
        model.load_state_dict(torch.load(MODEL_PATH, map_location='cpu', weights_only=True))
        model.eval()
        return model

    def _build_ui(self):
        # 상단 제목
        header = tk.Frame(self.root, bg=BG)
        header.pack(fill=tk.X, padx=20, pady=(15, 5))

        tk.Label(
            header, text='MNIST 숫자 인식',
            font=(FONT, 20, 'bold'), fg=FG, bg=BG
        ).pack(side=tk.LEFT)

        tk.Label(
            header, text='Convolutional Neural Network Visualization',
            font=(FONT, 11), fg=FG_SUB, bg=BG
        ).pack(side=tk.LEFT, padx=(12, 0), pady=(6, 0))

        # 구분선
        sep = tk.Frame(self.root, bg='#E0E0E0', height=1)
        sep.pack(fill=tk.X, padx=20, pady=(5, 10))

        # 메인 영역
        main_frame = tk.Frame(self.root, bg=BG)
        main_frame.pack(padx=15, pady=(0, 10))

        # ===== 왼쪽: 드로잉 =====
        left_frame = tk.Frame(main_frame, bg=BG)
        left_frame.pack(side=tk.LEFT, padx=(0, 15), anchor=tk.N)

        tk.Label(
            left_frame, text='숫자 그리기',
            font=(FONT, 13, 'bold'), fg=FG, bg=BG
        ).pack(anchor=tk.W, pady=(0, 5))

        self.drawing = DrawingCanvas(left_frame, on_draw_complete=self._on_recognize)
        self.drawing.frame.pack()

        # 버튼
        btn_frame = tk.Frame(left_frame, bg=BG)
        btn_frame.pack(pady=8, fill=tk.X)

        tk.Button(
            btn_frame, text='지우기', command=self._on_clear,
            font=(FONT, 10), bg='#F0F0F0', fg=FG,
            activebackground='#E0E0E0', activeforeground=FG,
            relief=tk.FLAT, padx=20, pady=4, cursor='hand2',
            highlightthickness=0
        ).pack(side=tk.LEFT, padx=(0, 8))

        tk.Button(
            btn_frame, text='인식하기', command=self._on_recognize,
            font=(FONT, 10), bg='#F0F0F0', fg=FG,
            activebackground='#E0E0E0', activeforeground=FG,
            relief=tk.FLAT, padx=20, pady=4, cursor='hand2',
            highlightthickness=0
        ).pack(side=tk.LEFT)

        # 예측 결과
        self.result_label = tk.Label(
            left_frame, text='숫자를 그려주세요',
            font=(FONT, 14), fg=FG_SUB, bg=BG
        )
        self.result_label.pack(pady=(5, 0))

        # 안내 텍스트
        tk.Label(
            left_frame, text='0 ~ 9 숫자를 적어보세요',
            font=(FONT, 10), fg='#BBBBBB', bg=BG
        ).pack(pady=(2, 0))

        # ===== 오른쪽: 시각화 =====
        right_frame = tk.Frame(main_frame, bg=BG)
        right_frame.pack(side=tk.LEFT, anchor=tk.N)

        tk.Label(
            right_frame, text='CNN 파이프라인',
            font=(FONT, 13, 'bold'), fg=FG, bg=BG
        ).pack(anchor=tk.W, pady=(0, 5))

        viz_frame = tk.Frame(right_frame, bg='white',
                             highlightbackground='#E0E0E0', highlightthickness=1)
        viz_frame.pack()
        self.visualizer = CNNVisualizer(viz_frame)

        # 컨트롤
        ctrl_frame = tk.Frame(right_frame, bg=BG)
        ctrl_frame.pack(pady=8, anchor=tk.W)

        tk.Button(
            ctrl_frame, text='다음 단계 (Space)', command=self._on_step,
            font=(FONT, 10), bg='#F0F0F0', fg=FG,
            activebackground='#E0E0E0', activeforeground=FG,
            relief=tk.FLAT, padx=20, pady=4, cursor='hand2',
            highlightthickness=0
        ).pack(side=tk.LEFT, padx=(0, 8))

        tk.Button(
            ctrl_frame, text='자동 재생', command=self._on_auto_play,
            font=(FONT, 10), bg='#F0F0F0', fg=FG,
            activebackground='#E0E0E0', activeforeground=FG,
            relief=tk.FLAT, padx=16, pady=4, cursor='hand2',
            highlightthickness=0
        ).pack(side=tk.LEFT, padx=(0, 8))

        tk.Button(
            ctrl_frame, text='처음부터', command=self._on_replay,
            font=(FONT, 10), bg='#F0F0F0', fg=FG,
            activebackground='#E0E0E0', activeforeground=FG,
            relief=tk.FLAT, padx=16, pady=4, cursor='hand2',
            highlightthickness=0
        ).pack(side=tk.LEFT)

    def _on_recognize(self):
        if self.drawing.is_empty():
            return

        pil_image = self.drawing.get_image()
        tensor, display_image = preprocess(pil_image)
        predicted, probabilities = self.model.get_prediction(tensor)

        confidence = probabilities[predicted]
        self.result_label.config(
            text=f'예측: {predicted}  ({confidence:.1%})',
            fg=FG, font=(FONT, 18, 'bold')
        )

        weights = {
            'conv1': self.model.conv1.weight.detach().cpu().numpy(),
            'conv2': self.model.conv2.weight.detach().cpu().numpy(),
        }
        self.visualizer.visualize(
            self.model.activations,
            display_image,
            predicted,
            probabilities,
            weights
        )

    def _on_clear(self):
        self.drawing.clear()
        self.result_label.config(
            text='숫자를 그려주세요',
            fg=FG_SUB, font=(FONT, 14)
        )

    def _on_replay(self):
        self.visualizer.replay()

    def _on_auto_play(self):
        self.visualizer.auto_play()

    def _on_step(self):
        self.visualizer.step_forward()

    def run(self):
        self.root.update_idletasks()
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (w // 2)
        y = (self.root.winfo_screenheight() // 2) - (h // 2)
        self.root.geometry(f'+{x}+{y}')
        self.root.mainloop()


if __name__ == '__main__':
    app = MNISTApp()
    app.run()
