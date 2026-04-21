"""
train_model.py — MNIST 데이터셋으로 CNN 모델을 학습하고 저장하는 스크립트

실행 방법:
    python train_model.py

처음 실행 시 MNIST 데이터셋을 자동으로 다운로드합니다. (~11MB)
학습 완료 후 saved_model/mnist_cnn.pth에 가중치를 저장합니다.
Apple Silicon Mac에서는 MPS(Metal) GPU를 사용하여 더 빠르게 학습합니다.
"""

import os
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

from model import SimpleCNN


def train():
    # ===== 설정 =====
    EPOCHS = 5           # 전체 데이터셋을 5번 반복 학습
    BATCH_SIZE = 64      # 한 번에 64개 이미지씩 학습
    LEARNING_RATE = 0.001
    SAVE_DIR = 'saved_model'
    SAVE_PATH = os.path.join(SAVE_DIR, 'mnist_cnn.pth')

    # 장치 선택: Apple Silicon MPS > NVIDIA CUDA > CPU
    if torch.backends.mps.is_available():
        device = torch.device('mps')      # 맥북 Apple Silicon GPU
    elif torch.cuda.is_available():
        device = torch.device('cuda')      # NVIDIA GPU
    else:
        device = torch.device('cpu')
    print(f'학습 장치: {device}')

    # ===== 데이터 준비 =====
    # MNIST 이미지를 텐서로 변환하고 정규화
    # mean=0.1307, std=0.3081은 MNIST 데이터셋의 통계값
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])

    # 학습 데이터 다운로드 (처음 실행 시에만)
    print('MNIST 데이터셋 준비 중...')
    train_dataset = datasets.MNIST(
        root='./data',
        train=True,
        download=True,
        transform=transform
    )

    # 테스트 데이터
    test_dataset = datasets.MNIST(
        root='./data',
        train=False,
        download=True,
        transform=transform
    )

    # DataLoader: 데이터를 배치 단위로 묶어서 제공
    train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)

    print(f'학습 데이터: {len(train_dataset)}장')
    print(f'테스트 데이터: {len(test_dataset)}장')

    # ===== 모델 생성 =====
    model = SimpleCNN().to(device)

    # 손실 함수: 분류 문제에 사용하는 CrossEntropyLoss
    criterion = nn.CrossEntropyLoss()

    # 옵티마이저: Adam (학습률 자동 조정)
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

    # ===== 학습 루프 =====
    print('\n학습 시작!')
    print('=' * 50)

    for epoch in range(1, EPOCHS + 1):
        model.train()  # 학습 모드
        running_loss = 0.0
        correct = 0
        total = 0

        for batch_idx, (images, labels) in enumerate(train_loader):
            images, labels = images.to(device), labels.to(device)

            # 1) 이전 그래디언트 초기화
            optimizer.zero_grad()

            # 2) 순전파: 이미지 → 모델 → 예측
            outputs = model(images)

            # 3) 손실 계산: 예측 vs 정답
            loss = criterion(outputs, labels)

            # 4) 역전파: 손실에서 그래디언트 계산
            loss.backward()

            # 5) 가중치 업데이트
            optimizer.step()

            # 통계 기록
            running_loss += loss.item()
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

            # 100 배치마다 진행 상황 출력
            if (batch_idx + 1) % 100 == 0:
                print(f'  Epoch {epoch}/{EPOCHS} | '
                      f'Batch {batch_idx + 1}/{len(train_loader)} | '
                      f'Loss: {loss.item():.4f}')

        # 에포크 결과
        epoch_loss = running_loss / len(train_loader)
        epoch_acc = 100 * correct / total
        print(f'\n  [Epoch {epoch}] 평균 손실: {epoch_loss:.4f} | '
              f'학습 정확도: {epoch_acc:.2f}%')

        # ===== 테스트 =====
        model.eval()  # 평가 모드
        test_correct = 0
        test_total = 0

        with torch.no_grad():  # 테스트 시에는 그래디언트 계산 불필요
            for images, labels in test_loader:
                images, labels = images.to(device), labels.to(device)
                outputs = model(images)
                _, predicted = torch.max(outputs, 1)
                test_total += labels.size(0)
                test_correct += (predicted == labels).sum().item()

        test_acc = 100 * test_correct / test_total
        print(f'  [Epoch {epoch}] 테스트 정확도: {test_acc:.2f}%')
        print('-' * 50)

    # ===== 모델 저장 =====
    os.makedirs(SAVE_DIR, exist_ok=True)
    torch.save(model.state_dict(), SAVE_PATH)
    print(f'\n모델이 {SAVE_PATH}에 저장되었습니다!')
    print(f'최종 테스트 정확도: {test_acc:.2f}%')


if __name__ == '__main__':
    train()
