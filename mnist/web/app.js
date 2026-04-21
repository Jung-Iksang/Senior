// ====== 전역 상태 ======
let session = null;       // ONNX 런타임 세션
let weights = null;       // 커널 가중치 JSON
let activations = null;   // 추론 결과 (중간 활성화)
let inputImage = null;    // 전처리된 28×28 입력
let probabilities = null; // softmax 확률
let predicted = -1;
let currentStep = -1;
let autoPlayTimer = null;

const LAYERS = [
    { name: 'Input',  color: '#4A90D9', desc: '입력: 손글씨 이미지 28×28' },
    { name: 'Conv1',  color: '#E8734A', desc: 'Conv1: 3×3 필터 8개로 합성곱 → 에지/선 감지' },
    { name: 'Pool1',  color: '#F5A623', desc: 'Pool1: 2×2 영역에서 최댓값 선택 → 크기 절반' },
    { name: 'Conv2',  color: '#E8734A', desc: 'Conv2: 3×3 필터 16개로 합성곱 → 곡선/형태 감지' },
    { name: 'Pool2',  color: '#F5A623', desc: 'Pool2: 2×2 맥스풀링 → 7×7로 압축' },
    { name: 'FC',     color: '#7ED321', desc: 'Flatten + FC: 7×7×16 = 784 → 64개 뉴런' },
    { name: 'Output', color: '#D0021B', desc: 'Output: 소프트맥스 → 숫자별 확률' },
];

// ====== 초기화 ======
window.addEventListener('DOMContentLoaded', async () => {
    setupCanvas();
    setupButtons();
    setupArchBar();
    await loadModel();
});

async function loadModel() {
    try {
        session = await ort.InferenceSession.create('./model.onnx');
        const resp = await fetch('./weights.json');
        weights = await resp.json();
        console.log('모델 로드 완료');
    } catch (e) {
        console.error('모델 로드 실패:', e);
        document.getElementById('prediction').textContent = '모델 로드 실패 — 콘솔 확인';
    }
}

// ====== 드로잉 캔버스 ======
function setupCanvas() {
    const canvas = document.getElementById('drawCanvas');
    const ctx = canvas.getContext('2d');
    ctx.fillStyle = '#fff';
    ctx.fillRect(0, 0, 280, 280);
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';
    ctx.lineWidth = 24;
    ctx.strokeStyle = '#000';

    let drawing = false;
    let lastX, lastY;

    function startDraw(x, y) {
        drawing = true;
        lastX = x; lastY = y;
        ctx.beginPath();
        ctx.arc(x, y, 12, 0, Math.PI * 2);
        ctx.fillStyle = '#000';
        ctx.fill();
    }
    function draw(x, y) {
        if (!drawing) return;
        ctx.beginPath();
        ctx.moveTo(lastX, lastY);
        ctx.lineTo(x, y);
        ctx.stroke();
        lastX = x; lastY = y;
    }
    function stopDraw() {
        if (drawing) { drawing = false; recognize(); }
    }

    // 마우스
    canvas.addEventListener('mousedown', e => startDraw(e.offsetX, e.offsetY));
    canvas.addEventListener('mousemove', e => draw(e.offsetX, e.offsetY));
    canvas.addEventListener('mouseup', stopDraw);
    canvas.addEventListener('mouseleave', stopDraw);

    // 터치
    canvas.addEventListener('touchstart', e => {
        e.preventDefault();
        const r = canvas.getBoundingClientRect();
        const t = e.touches[0];
        startDraw(t.clientX - r.left, t.clientY - r.top);
    });
    canvas.addEventListener('touchmove', e => {
        e.preventDefault();
        const r = canvas.getBoundingClientRect();
        const t = e.touches[0];
        draw(t.clientX - r.left, t.clientY - r.top);
    });
    canvas.addEventListener('touchend', e => { e.preventDefault(); stopDraw(); });
}

function clearCanvas() {
    const canvas = document.getElementById('drawCanvas');
    const ctx = canvas.getContext('2d');
    ctx.fillStyle = '#fff';
    ctx.fillRect(0, 0, 280, 280);
    document.getElementById('prediction').textContent = '0 ~ 9 숫자를 적어보세요';
    document.getElementById('prediction').className = 'prediction';
    document.getElementById('detailView').innerHTML = '<p class="detail-placeholder">숫자를 그리면 CNN의 동작 과정을 단계별로 보여드립니다</p>';
    activations = null;
    currentStep = -1;
    stopAutoPlay();
    updateArchBar(-1);
}

// ====== 전처리 ======
function preprocessCanvas() {
    const canvas = document.getElementById('drawCanvas');
    const ctx = canvas.getContext('2d');
    const imgData = ctx.getImageData(0, 0, 280, 280);
    const pixels = imgData.data;

    // RGBA → grayscale (흰 배경/검정 글씨 → 반전 → MNIST 형식)
    const gray = new Float32Array(280 * 280);
    for (let i = 0; i < 280 * 280; i++) {
        gray[i] = 1.0 - (pixels[i * 4] / 255.0); // 반전
    }

    // 바운딩 박스 찾기
    let minR = 280, maxR = 0, minC = 280, maxC = 0;
    for (let r = 0; r < 280; r++) {
        for (let c = 0; c < 280; c++) {
            if (gray[r * 280 + c] > 0.01) {
                minR = Math.min(minR, r); maxR = Math.max(maxR, r);
                minC = Math.min(minC, c); maxC = Math.max(maxC, c);
            }
        }
    }

    if (minR >= maxR) return null; // 빈 캔버스

    // 숫자 영역 crop + 20×20에 맞춤 + 28×28 중앙 배치
    const cropH = maxR - minR + 1;
    const cropW = maxC - minC + 1;
    const scale = 20.0 / Math.max(cropH, cropW);
    const newH = Math.round(cropH * scale);
    const newW = Math.round(cropW * scale);

    // 임시 캔버스로 리사이즈
    const tmpCanvas = document.createElement('canvas');
    tmpCanvas.width = 28; tmpCanvas.height = 28;
    const tmpCtx = tmpCanvas.getContext('2d');

    // crop 영역을 별도 캔버스에 그리기
    const cropCanvas = document.createElement('canvas');
    cropCanvas.width = cropW; cropCanvas.height = cropH;
    const cropCtx = cropCanvas.getContext('2d');
    const cropImgData = cropCtx.createImageData(cropW, cropH);
    for (let r = 0; r < cropH; r++) {
        for (let c = 0; c < cropW; c++) {
            const v = Math.round(gray[(minR + r) * 280 + (minC + c)] * 255);
            const idx = (r * cropW + c) * 4;
            cropImgData.data[idx] = v;
            cropImgData.data[idx + 1] = v;
            cropImgData.data[idx + 2] = v;
            cropImgData.data[idx + 3] = 255;
        }
    }
    cropCtx.putImageData(cropImgData, 0, 0);

    // 28×28 중앙에 배치
    const offX = Math.round((28 - newW) / 2);
    const offY = Math.round((28 - newH) / 2);
    tmpCtx.fillStyle = '#000';
    tmpCtx.fillRect(0, 0, 28, 28);
    tmpCtx.drawImage(cropCanvas, 0, 0, cropW, cropH, offX, offY, newW, newH);

    // 28×28 → float 배열
    const finalData = tmpCtx.getImageData(0, 0, 28, 28);
    const result = new Float32Array(28 * 28);
    for (let i = 0; i < 28 * 28; i++) {
        result[i] = finalData.data[i * 4] / 255.0;
    }

    // MNIST 정규화
    const MEAN = 0.1307, STD = 0.3081;
    const normalized = new Float32Array(28 * 28);
    for (let i = 0; i < 28 * 28; i++) {
        normalized[i] = (result[i] - MEAN) / STD;
    }

    inputImage = result; // 0~1 범위 (시각화용)
    return normalized;
}

// ====== ONNX 추론 ======
async function recognize() {
    if (!session) return;
    const input = preprocessCanvas();
    if (!input) return;

    const tensor = new ort.Tensor('float32', input, [1, 1, 28, 28]);
    const results = await session.run({ input: tensor });

    // 활성화 저장
    activations = {
        relu1: results.relu1,
        pool1: results.pool1,
        relu2: results.relu2,
        pool2: results.pool2,
        fc1: results.fc1,
        fc2: results.fc2,
    };

    // softmax
    const fc2 = results.fc2.data;
    const maxVal = Math.max(...fc2);
    const exps = fc2.map(v => Math.exp(v - maxVal));
    const sumExp = exps.reduce((a, b) => a + b, 0);
    probabilities = exps.map(v => v / sumExp);
    predicted = probabilities.indexOf(Math.max(...probabilities));

    // 결과 표시
    const pred = document.getElementById('prediction');
    pred.textContent = `예측: ${predicted}  (${(probabilities[predicted] * 100).toFixed(1)}%)`;
    pred.className = 'prediction active';

    // 첫 단계 표시
    currentStep = 0;
    showStep(0);
}

// ====== 단계별 제어 ======
function showStep(step) {
    if (!activations || step < 0 || step > 6) return;
    currentStep = step;
    updateArchBar(step);

    const view = document.getElementById('detailView');
    view.innerHTML = '';

    switch (step) {
        case 0: renderInput(view); break;
        case 1: renderConv(view, 1); break;
        case 2: renderPool(view, 2); break;
        case 3: renderConv(view, 3); break;
        case 4: renderPool(view, 4); break;
        case 5: renderFlattenFC(view); break;
        case 6: renderOutput(view); break;
    }
}

function nextStep() {
    if (!activations) return;
    stopAutoPlay();
    if (currentStep < 6) showStep(currentStep + 1);
}

function autoPlay() {
    if (!activations) return;
    stopAutoPlay();
    autoPlayTimer = setInterval(() => {
        if (currentStep >= 6) { stopAutoPlay(); return; }
        showStep(currentStep + 1);
    }, 800);
}

function replay() {
    if (!activations) return;
    currentStep = -1;
    autoPlay();
}

function stopAutoPlay() {
    if (autoPlayTimer) { clearInterval(autoPlayTimer); autoPlayTimer = null; }
}

// ====== 아키텍처 바 업데이트 ======
function updateArchBar(activeIdx) {
    document.querySelectorAll('.arch-layer').forEach(el => {
        const idx = parseInt(el.dataset.layer);
        el.classList.remove('active', 'past');
        if (idx === activeIdx) el.classList.add('active');
        else if (idx < activeIdx) el.classList.add('past');
    });
}

function setupArchBar() {
    document.querySelectorAll('.arch-layer').forEach(el => {
        el.addEventListener('click', () => {
            if (!activations) return;
            stopAutoPlay();
            showStep(parseInt(el.dataset.layer));
        });
    });
}

function setupButtons() {
    document.getElementById('btnClear').addEventListener('click', clearCanvas);
    document.getElementById('btnRecognize').addEventListener('click', recognize);
    document.getElementById('btnStep').addEventListener('click', nextStep);
    document.getElementById('btnAutoPlay').addEventListener('click', autoPlay);
    document.getElementById('btnReplay').addEventListener('click', replay);
    document.addEventListener('keydown', e => {
        if (e.code === 'Space') { e.preventDefault(); nextStep(); }
    });
}

// ====== 유틸 ======
function drawArray2D(canvas, data, rows, cols, cmap = 'blues') {
    canvas.width = cols; canvas.height = rows;
    const ctx = canvas.getContext('2d');
    const imgData = ctx.createImageData(cols, rows);
    let min = Infinity, max = -Infinity;
    for (let i = 0; i < data.length; i++) { min = Math.min(min, data[i]); max = Math.max(max, data[i]); }
    if (max <= min) max = min + 1;

    for (let i = 0; i < rows * cols; i++) {
        const v = (data[i] - min) / (max - min);
        let r, g, b;
        if (cmap === 'gray') { r = g = b = Math.round(v * 255); }
        else if (cmap === 'blues') { r = Math.round(255 - v * 200); g = Math.round(255 - v * 150); b = 255; }
        else if (cmap === 'rdbu') {
            if (v < 0.5) { r = Math.round(200 * (1 - v * 2)); g = Math.round(100 * (1 - v * 2)); b = Math.round(255 * v * 2); }
            else { r = Math.round(255 * (v - 0.5) * 2); g = Math.round(100 * (v - 0.5) * 2); b = Math.round(200 * (1 - (v - 0.5) * 2)); }
        }
        else { r = g = b = Math.round(v * 255); }
        imgData.data[i * 4] = r; imgData.data[i * 4 + 1] = g; imgData.data[i * 4 + 2] = b; imgData.data[i * 4 + 3] = 255;
    }
    ctx.putImageData(imgData, 0, 0);
}

function getActivation(key) {
    const t = activations[key];
    return { data: Array.from(t.data), dims: t.dims };
}

// ====== 렌더: Input ======
function renderInput(view) {
    const title = document.createElement('div');
    title.className = 'detail-title'; title.style.color = LAYERS[0].color;
    title.textContent = LAYERS[0].desc;
    view.appendChild(title);

    const wrap = document.createElement('div');
    wrap.style.cssText = 'display:flex; gap:24px; align-items:flex-start;';

    const canvas = document.createElement('canvas');
    canvas.style.cssText = 'width:180px; height:180px; image-rendering:pixelated; border:1px solid #ddd;';
    drawArray2D(canvas, inputImage, 28, 28, 'gray');
    wrap.appendChild(canvas);

    const info = document.createElement('div');
    info.innerHTML = `<p style="font-size:13px; color:#444; line-height:1.8;">
        <b>입력 데이터</b><br><br>
        • 손으로 그린 숫자를 28×28 픽셀로 변환<br>
        • 숫자를 이미지 중앙에 정렬<br>
        • MNIST 데이터셋과 동일하게 정규화<br>
        • 1개 채널 (흑백) 이미지<br><br>
        → 이 28×28 = 784개의 픽셀값이<br>
        &nbsp;&nbsp;첫 번째 합성곱 레이어의 입력이 됩니다.</p>`;
    wrap.appendChild(info);
    view.appendChild(wrap);
}

// ====== 렌더: Conv (커널 슬라이딩 애니메이션) ======
function renderConv(view, step) {
    const layer = LAYERS[step];
    const title = document.createElement('div');
    title.className = 'detail-title'; title.style.color = layer.color;
    title.textContent = layer.desc;
    view.appendChild(title);

    const wrap = document.createElement('div');
    wrap.className = 'conv-detail';

    // 입력 이미지 + 슬라이딩 커널
    const inputDiv = document.createElement('div');
    inputDiv.className = 'conv-input';
    const inputCanvas = document.createElement('canvas');
    inputCanvas.style.cssText = 'width:140px; height:140px; image-rendering:pixelated;';

    let inputData, inH, inW;
    if (step === 1) {
        inputData = inputImage; inH = 28; inW = 28;
    } else {
        const a = getActivation('pool1'); inH = a.dims[2]; inW = a.dims[3];
        inputData = a.data.slice(0, inH * inW);
    }
    drawArray2D(inputCanvas, inputData, inH, inW, 'gray');
    inputDiv.appendChild(inputCanvas);

    // 슬라이딩 커널 박스
    const kernelBox = document.createElement('div');
    kernelBox.className = 'sliding-kernel';
    const scale = 140 / inH;
    kernelBox.style.width = (3 * scale) + 'px';
    kernelBox.style.height = (3 * scale) + 'px';
    kernelBox.style.left = '0px'; kernelBox.style.top = '0px';
    inputDiv.appendChild(kernelBox);

    const inputLabel = document.createElement('div');
    inputLabel.className = 'conv-label';
    inputLabel.textContent = `입력 (${inH}×${inW})`;
    inputDiv.appendChild(inputLabel);
    wrap.appendChild(inputDiv);

    // 슬라이딩 애니메이션
    let pos = 0;
    const maxPos = (inH - 3 + 1) * (inW - 3 + 1);
    const slideInterval = setInterval(() => {
        const row = Math.floor(pos / (inW - 2));
        const col = pos % (inW - 2);
        kernelBox.style.left = (col * scale) + 'px';
        kernelBox.style.top = (row * scale) + 'px';
        pos = (pos + 1) % maxPos;
    }, 50);

    // cleanup on next step
    const origShowStep = window._cleanupConv;
    if (origShowStep) origShowStep();
    window._cleanupConv = () => clearInterval(slideInterval);

    // 화살표
    const arrow1 = document.createElement('div');
    arrow1.className = 'conv-arrow'; arrow1.textContent = '✱';
    wrap.appendChild(arrow1);

    // 커널 가중치
    const kernelDiv = document.createElement('div');
    kernelDiv.className = 'conv-kernels';
    const kKey = step === 1 ? 'conv1_kernels' : 'conv2_kernels';
    const kernels = weights[kKey];
    const showK = Math.min(kernels.length, 4);

    const kGrid = document.createElement('div');
    kGrid.className = 'kernel-grid';
    kGrid.style.gridTemplateColumns = `repeat(2, 40px)`;
    for (let k = 0; k < showK; k++) {
        const item = document.createElement('div');
        const kCanvas = document.createElement('canvas');
        kCanvas.style.cssText = 'width:36px; height:36px; image-rendering:pixelated;';
        const kData = kernels[k][0].flat();
        drawArray2D(kCanvas, kData, 3, 3, 'rdbu');
        item.appendChild(kCanvas);
        const label = document.createElement('div');
        label.className = 'kernel-label'; label.textContent = `필터${k+1}`;
        item.appendChild(label);
        kGrid.appendChild(item);
    }
    kernelDiv.appendChild(kGrid);
    const kLabel = document.createElement('div');
    kLabel.className = 'conv-label';
    kLabel.textContent = `3×3 커널 (${kernels.length}개)`;
    kernelDiv.appendChild(kLabel);
    wrap.appendChild(kernelDiv);

    // 화살표
    const arrow2 = document.createElement('div');
    arrow2.className = 'conv-arrow'; arrow2.textContent = '→';
    wrap.appendChild(arrow2);

    // 출력 feature maps
    const outDiv = document.createElement('div');
    outDiv.className = 'conv-output';
    const actKey = step === 1 ? 'relu1' : 'relu2';
    const act = getActivation(actKey);
    const nMaps = act.dims[1], outH = act.dims[2], outW = act.dims[3];
    const mapSize = outH * outW;

    const fGrid = document.createElement('div');
    fGrid.className = 'fmap-grid';
    const cols = nMaps <= 8 ? 4 : 4;
    fGrid.style.gridTemplateColumns = `repeat(${cols}, 48px)`;
    for (let m = 0; m < nMaps; m++) {
        const item = document.createElement('div');
        item.className = 'fmap-item';
        const fCanvas = document.createElement('canvas');
        fCanvas.style.cssText = 'width:44px; height:44px; image-rendering:pixelated;';
        drawArray2D(fCanvas, act.data.slice(m * mapSize, (m + 1) * mapSize), outH, outW, 'blues');
        item.appendChild(fCanvas);
        const label = document.createElement('span');
        label.textContent = `${m+1}`;
        item.appendChild(label);
        fGrid.appendChild(item);
    }
    outDiv.appendChild(fGrid);
    const outLabel = document.createElement('div');
    outLabel.className = 'conv-label';
    outLabel.textContent = `출력 (${outH}×${outW}×${nMaps})`;
    outDiv.appendChild(outLabel);
    wrap.appendChild(outDiv);

    view.appendChild(wrap);
}

// ====== 렌더: Pool (전후 비교) ======
function renderPool(view, step) {
    const layer = LAYERS[step];
    const title = document.createElement('div');
    title.className = 'detail-title'; title.style.color = layer.color;
    title.textContent = layer.desc;
    view.appendChild(title);

    const beforeKey = step === 2 ? 'relu1' : 'relu2';
    const afterKey = step === 2 ? 'pool1' : 'pool2';
    const before = getActivation(beforeKey);
    const after = getActivation(afterKey);
    const nMaps = before.dims[1];
    const bH = before.dims[2], bW = before.dims[3];
    const aH = after.dims[2], aW = after.dims[3];
    const bSize = bH * bW, aSize = aH * aW;

    // 상단: 대표 비교 (3개)
    const compareDiv = document.createElement('div');
    compareDiv.style.cssText = 'display:flex; gap:12px; align-items:center; margin-bottom:16px; flex-wrap:wrap;';

    for (let i = 0; i < Math.min(3, nMaps); i++) {
        const bCanvas = document.createElement('canvas');
        bCanvas.style.cssText = 'width:80px; height:80px; image-rendering:pixelated; border:1px solid #ddd;';
        drawArray2D(bCanvas, before.data.slice(i * bSize, (i + 1) * bSize), bH, bW, 'blues');

        if (i === 0) {
            const label = document.createElement('div');
            label.style.cssText = 'text-align:center;';
            label.innerHTML = `<div style="font-size:10px; color:#E8734A; margin-bottom:2px;">전 (${bH}×${bW})</div>`;
            label.appendChild(bCanvas);
            compareDiv.appendChild(label);
        } else {
            compareDiv.appendChild(bCanvas);
        }
    }

    const arrow = document.createElement('div');
    arrow.style.cssText = 'font-size:13px; font-weight:700; color:' + layer.color + '; text-align:center; padding:0 8px;';
    arrow.innerHTML = '→<br><span style="font-size:10px;">Max Pool<br>2×2</span>';
    compareDiv.appendChild(arrow);

    for (let i = 0; i < Math.min(3, nMaps); i++) {
        const aCanvas = document.createElement('canvas');
        aCanvas.style.cssText = 'width:56px; height:56px; image-rendering:pixelated; border:1px solid #ddd;';
        drawArray2D(aCanvas, after.data.slice(i * aSize, (i + 1) * aSize), aH, aW, 'blues');

        if (i === 0) {
            const label = document.createElement('div');
            label.style.cssText = 'text-align:center;';
            label.innerHTML = `<div style="font-size:10px; color:${layer.color}; margin-bottom:2px;">후 (${aH}×${aW})</div>`;
            label.appendChild(aCanvas);
            compareDiv.appendChild(label);
        } else {
            compareDiv.appendChild(aCanvas);
        }
    }
    view.appendChild(compareDiv);

    // 하단: 전체 그리드
    const gridLabel = document.createElement('div');
    gridLabel.style.cssText = 'font-size:11px; color:#999; margin-bottom:6px;';
    gridLabel.textContent = `풀링 후 전체 feature maps (${nMaps}개)`;
    view.appendChild(gridLabel);

    const grid = document.createElement('div');
    grid.className = 'fmap-grid';
    grid.style.gridTemplateColumns = `repeat(${Math.min(nMaps, 8)}, 40px)`;
    for (let m = 0; m < nMaps; m++) {
        const item = document.createElement('div');
        item.className = 'fmap-item';
        const c = document.createElement('canvas');
        c.style.cssText = 'width:36px; height:36px; image-rendering:pixelated;';
        drawArray2D(c, after.data.slice(m * aSize, (m + 1) * aSize), aH, aW, 'blues');
        item.appendChild(c);
        const s = document.createElement('span'); s.textContent = `${m+1}`;
        item.appendChild(s);
        grid.appendChild(item);
    }
    view.appendChild(grid);
}

// ====== 렌더: Flatten + FC (2D→1D 애니메이션) ======
function renderFlattenFC(view) {
    const layer = LAYERS[5];
    const title = document.createElement('div');
    title.className = 'detail-title'; title.style.color = layer.color;
    title.textContent = layer.desc;
    view.appendChild(title);

    const wrap = document.createElement('div');
    wrap.className = 'fc-detail';

    // 왼쪽: Pool2 feature maps (4×4 그리드)
    const pool2Div = document.createElement('div');
    pool2Div.style.cssText = 'text-align:center;';
    const pool2 = getActivation('pool2');
    const pH = pool2.dims[2], pW = pool2.dims[3], pSize = pH * pW;
    const nMaps = pool2.dims[1];

    const pGrid = document.createElement('div');
    pGrid.style.cssText = 'display:grid; grid-template-columns:repeat(4,30px); gap:2px;';
    for (let m = 0; m < nMaps; m++) {
        const c = document.createElement('canvas');
        c.style.cssText = 'width:28px; height:28px; image-rendering:pixelated; border:1px solid #eee;';
        drawArray2D(c, pool2.data.slice(m * pSize, (m + 1) * pSize), pH, pW, 'blues');
        pGrid.appendChild(c);
    }
    pool2Div.appendChild(pGrid);
    pool2Div.innerHTML += `<div style="font-size:10px; color:#999; margin-top:4px;">Pool2 (7×7×16)</div>`;
    wrap.appendChild(pool2Div);

    // 화살표 + Flatten
    const flatDiv = document.createElement('div');
    flatDiv.style.cssText = 'text-align:center; padding:0 10px;';
    flatDiv.innerHTML = `<div style="font-size:20px; color:${layer.color};">→</div>
        <div style="font-size:10px; color:#888; margin-top:4px;">Flatten<br>7×7×16<br>= 784</div>`;

    // 1D 스트립 시각화
    const stripCanvas = document.createElement('canvas');
    stripCanvas.style.cssText = 'width:20px; height:200px; image-rendering:pixelated; border:1px solid #ddd; margin-top:8px;';
    const flatData = pool2.data;
    drawArray2D(stripCanvas, flatData, flatData.length, 1, 'blues');
    flatDiv.appendChild(stripCanvas);
    wrap.appendChild(flatDiv);

    // 화살표
    const arrow2 = document.createElement('div');
    arrow2.style.cssText = 'font-size:20px; color:' + layer.color + '; align-self:center;';
    arrow2.textContent = '→';
    wrap.appendChild(arrow2);

    // FC 바 차트
    const fcDiv = document.createElement('div');
    fcDiv.style.cssText = 'flex:1;';
    const fc1 = getActivation('fc1');
    const fcData = fc1.data;

    const fcCanvas = document.createElement('canvas');
    fcCanvas.width = 500; fcCanvas.height = 200;
    fcCanvas.style.cssText = 'width:100%; height:200px;';
    const ctx = fcCanvas.getContext('2d');
    ctx.fillStyle = '#fff'; ctx.fillRect(0, 0, 500, 200);

    const barW = 500 / fcData.length;
    const maxAbs = Math.max(...fcData.map(Math.abs), 0.001);
    const midY = 100;
    for (let i = 0; i < fcData.length; i++) {
        const v = fcData[i];
        const barH = (Math.abs(v) / maxAbs) * 90;
        ctx.fillStyle = v > 0 ? '#4ECDC4' : '#FF6B6B';
        if (v > 0) ctx.fillRect(i * barW, midY - barH, barW - 1, barH);
        else ctx.fillRect(i * barW, midY, barW - 1, barH);
    }
    ctx.strokeStyle = '#ddd'; ctx.beginPath(); ctx.moveTo(0, midY); ctx.lineTo(500, midY); ctx.stroke();
    fcDiv.appendChild(fcCanvas);

    const nActive = fcData.filter(v => v > 0).length;
    fcDiv.innerHTML += `<div style="font-size:10px; color:#888; margin-top:4px;">FC 활성화 (64개 뉴런, 활성: ${nActive}개) — 초록:양수, 빨강:음수</div>`;
    wrap.appendChild(fcDiv);

    view.appendChild(wrap);
}

// ====== 렌더: Output ======
function renderOutput(view) {
    const layer = LAYERS[6];
    const title = document.createElement('div');
    title.className = 'detail-title'; title.style.color = layer.color;
    title.textContent = `예측: ${predicted}  (확신도 ${(probabilities[predicted]*100).toFixed(1)}%)`;
    view.appendChild(title);

    const wrap = document.createElement('div');
    wrap.className = 'output-detail';

    for (let d = 0; d < 10; d++) {
        const bar = document.createElement('div');
        bar.className = 'output-bar';

        const digit = document.createElement('div');
        digit.className = 'output-digit' + (d === predicted ? ' predicted' : '');
        digit.textContent = d;

        const fillBg = document.createElement('div');
        fillBg.className = 'output-fill-bg';
        const fill = document.createElement('div');
        fill.className = 'output-fill ' + (d === predicted ? 'predicted' : 'other');
        fill.style.width = '0%';
        fillBg.appendChild(fill);

        const prob = document.createElement('div');
        prob.className = 'output-prob' + (d === predicted ? ' predicted' : '');
        prob.textContent = (probabilities[d] * 100).toFixed(1) + '%';

        bar.appendChild(digit);
        bar.appendChild(fillBg);
        bar.appendChild(prob);
        wrap.appendChild(bar);

        // 애니메이션
        requestAnimationFrame(() => {
            fill.style.width = (probabilities[d] * 100) + '%';
        });
    }
    view.appendChild(wrap);
}
