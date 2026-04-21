"""
model.py — MNIST 숫자 인식을 위한 간단한 CNN 모델

구조:
    Input (1x28x28)
    → Conv2d(8 filters) → ReLU → MaxPool2d
    → Conv2d(16 filters) → ReLU → MaxPool2d
    → Flatten → Linear(64) → ReLU → Linear(10)

시각화를 위해 의도적으로 작은 모델을 사용합니다.
8개, 16개 필터만 사용하여 모든 feature map을 화면에 표시할 수 있습니다.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F


class SimpleCNN(nn.Module):
    """MNIST 숫자 인식 CNN 모델 (시각화 기능 포함)"""

    def __init__(self):
        super().__init__()

        # 중간 레이어 활성화를 저장할 딕셔너리
        self.activations = {}

        # ===== 합성곱 레이어 =====
        # Conv1: 1채널 입력 → 8개 필터, 3x3 커널, 패딩으로 크기 유지
        # 입력: (1, 28, 28) → 출력: (8, 28, 28)
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=8, kernel_size=3, padding=1)

        # Conv2: 8채널 입력 → 16개 필터
        # 입력: (8, 14, 14) → 출력: (16, 14, 14)
        self.conv2 = nn.Conv2d(in_channels=8, out_channels=16, kernel_size=3, padding=1)

        # ===== 풀링 레이어 =====
        # 2x2 맥스 풀링: 크기를 절반으로 줄임
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)

        # ===== 완전연결 레이어 =====
        # Pool2 출력: (16, 7, 7) = 784 → 64
        self.fc1 = nn.Linear(16 * 7 * 7, 64)

        # 64 → 10 (숫자 0~9)
        self.fc2 = nn.Linear(64, 10)

        # forward hook 등록
        self._register_hooks()

    def _register_hooks(self):
        """각 레이어에 forward hook을 등록하여 중간 활성화를 캡처합니다."""

        def make_hook(name):
            def hook(module, input, output):
                self.activations[name] = output.detach().cpu()
            return hook

        self.conv1.register_forward_hook(make_hook('conv1'))
        self.conv2.register_forward_hook(make_hook('conv2'))

    def forward(self, x):
        """
        순전파 과정 (각 단계의 활성화가 self.activations에 자동 저장됩니다)

        Args:
            x: 입력 텐서 (batch, 1, 28, 28)

        Returns:
            출력 텐서 (batch, 10) — 각 숫자에 대한 점수
        """
        # Conv1 → ReLU → Pool1
        x = self.conv1(x)                          # (batch, 8, 28, 28)
        x = F.relu(x)
        self.activations['relu1'] = x.detach().cpu()
        x = self.pool(x)                            # (batch, 8, 14, 14)
        self.activations['pool1'] = x.detach().cpu()

        # Conv2 → ReLU → Pool2
        x = self.conv2(x)                           # (batch, 16, 14, 14)
        x = F.relu(x)
        self.activations['relu2'] = x.detach().cpu()
        x = self.pool(x)                            # (batch, 16, 7, 7)
        self.activations['pool2'] = x.detach().cpu()

        # Flatten → FC1 → ReLU → FC2
        x = x.view(x.size(0), -1)                   # (batch, 784)
        x = self.fc1(x)                              # (batch, 64)
        x = F.relu(x)
        self.activations['fc1'] = x.detach().cpu()
        x = self.fc2(x)                              # (batch, 10)
        self.activations['fc2'] = x.detach().cpu()

        return x

    def get_prediction(self, x):
        """
        예측 결과와 확률을 반환합니다.

        Args:
            x: 입력 텐서 (1, 1, 28, 28)

        Returns:
            (예측 숫자, 확률 배열) 튜플
        """
        self.eval()
        with torch.no_grad():
            output = self.forward(x)
            probabilities = F.softmax(output.cpu(), dim=1)
            predicted = torch.argmax(probabilities, dim=1).item()
            return predicted, probabilities.squeeze().numpy()
