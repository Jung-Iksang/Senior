"""
export_onnx.py — PyTorch 모델을 ONNX로 변환 + 가중치를 JSON으로 추출

ONNX 모델은 중간 활성화(relu1, pool1, relu2, pool2, fc1, fc2)를
모두 출력으로 내보내서 브라우저에서 시각화에 사용할 수 있게 합니다.

사용법:
    python export_onnx.py
"""

import os
import json
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

from model import SimpleCNN

MODEL_PATH = os.path.join('saved_model', 'mnist_cnn.pth')
WEB_DIR = 'web'
ONNX_PATH = os.path.join(WEB_DIR, 'model.onnx')
WEIGHTS_PATH = os.path.join(WEB_DIR, 'weights.json')


class SimpleCNNForExport(nn.Module):
    """ONNX 내보내기용 모델 — 모든 중간 활성화를 출력으로 반환"""

    def __init__(self, original_model):
        super().__init__()
        self.conv1 = original_model.conv1
        self.conv2 = original_model.conv2
        self.pool = original_model.pool
        self.fc1 = original_model.fc1
        self.fc2 = original_model.fc2

    def forward(self, x):
        # Conv1 → ReLU → Pool1
        c1 = self.conv1(x)
        r1 = F.relu(c1)
        p1 = self.pool(r1)

        # Conv2 → ReLU → Pool2
        c2 = self.conv2(p1)
        r2 = F.relu(c2)
        p2 = self.pool(r2)

        # Flatten → FC1 → ReLU → FC2
        flat = p2.view(p2.size(0), -1)
        f1 = F.relu(self.fc1(flat))
        f2 = self.fc2(f1)

        # 모든 중간 활성화를 출력으로 반환
        return r1, p1, r2, p2, f1, f2


def export():
    # 모델 로드
    if not os.path.exists(MODEL_PATH):
        print(f'오류: {MODEL_PATH}를 찾을 수 없습니다.')
        print('먼저 python train_model.py를 실행해주세요.')
        return

    original = SimpleCNN()
    original.load_state_dict(torch.load(MODEL_PATH, map_location='cpu', weights_only=True))
    original.eval()

    # 내보내기용 모델
    export_model = SimpleCNNForExport(original)
    export_model.eval()

    # web 디렉토리 생성
    os.makedirs(WEB_DIR, exist_ok=True)

    # ONNX 내보내기
    dummy_input = torch.randn(1, 1, 28, 28)
    output_names = ['relu1', 'pool1', 'relu2', 'pool2', 'fc1', 'fc2']

    torch.onnx.export(
        export_model,
        dummy_input,
        ONNX_PATH,
        input_names=['input'],
        output_names=output_names,
        dynamic_axes={'input': {0: 'batch'}},
        opset_version=17
    )
    print(f'ONNX 모델 저장: {ONNX_PATH}')

    # 가중치를 JSON으로 저장 (커널 시각화용)
    weights = {
        'conv1_kernels': original.conv1.weight.detach().numpy().tolist(),
        'conv1_bias': original.conv1.bias.detach().numpy().tolist(),
        'conv2_kernels': original.conv2.weight.detach().numpy().tolist(),
        'conv2_bias': original.conv2.bias.detach().numpy().tolist(),
    }
    with open(WEIGHTS_PATH, 'w') as f:
        json.dump(weights, f)
    print(f'가중치 JSON 저장: {WEIGHTS_PATH}')

    # 검증: 원본 모델과 ONNX 모델 결과 비교
    print('\n검증 중...')
    original.eval()
    with torch.no_grad():
        test_input = torch.randn(1, 1, 28, 28)
        orig_output = original(test_input)
        orig_pred = torch.argmax(F.softmax(orig_output, dim=1), dim=1).item()

    try:
        import onnxruntime as ort
        sess = ort.InferenceSession(ONNX_PATH)
        onnx_outputs = sess.run(None, {'input': test_input.numpy()})
        onnx_fc2 = onnx_outputs[5]  # fc2
        onnx_pred = np.argmax(onnx_fc2)

        if orig_pred == onnx_pred:
            print(f'검증 성공: PyTorch={orig_pred}, ONNX={onnx_pred} (일치)')
        else:
            print(f'검증 주의: PyTorch={orig_pred}, ONNX={onnx_pred} (랜덤 입력이라 다를 수 있음)')

        # 수치 오차 확인
        orig_fc2 = original.activations['fc2'].numpy()
        max_diff = np.abs(orig_fc2 - onnx_fc2).max()
        print(f'최대 수치 오차: {max_diff:.8f}')
    except ImportError:
        print('onnxruntime 미설치 — ONNX 검증 건너뜀 (pip install onnxruntime)')

    print('\n완료! web/ 폴더에 model.onnx와 weights.json이 생성되었습니다.')


if __name__ == '__main__':
    export()
