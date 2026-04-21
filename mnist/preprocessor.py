"""
preprocessor.py — 캔버스에서 그린 이미지를 CNN 입력 텐서로 변환

주요 처리 과정:
    1. 280x280 PIL Image → 숫자 영역 crop
    2. 중심 정렬 (MNIST 데이터와 동일하게)
    3. 28x28로 리사이즈
    4. 정규화 후 PyTorch 텐서로 변환
"""

import numpy as np
from PIL import Image
import torch


# MNIST 데이터셋의 평균과 표준편차
MNIST_MEAN = 0.1307
MNIST_STD = 0.3081


def preprocess(pil_image):
    """
    PIL Image를 CNN 입력 텐서로 변환합니다.

    Args:
        pil_image: PIL Image (280x280, grayscale, 검은 배경에 흰 글씨)

    Returns:
        (tensor, display_image) 튜플
        - tensor: (1, 1, 28, 28) PyTorch 텐서 (정규화됨)
        - display_image: (28, 28) NumPy 배열 (시각화용, 0~1 범위)
    """
    # 1) numpy 배열로 변환
    img_array = np.array(pil_image, dtype=np.float32)

    # 2) 숫자가 그려진 영역 찾기 (bounding box)
    img_centered = center_digit(img_array)

    # 3) 28x28로 리사이즈
    img_resized = np.array(
        Image.fromarray(img_centered.astype(np.uint8)).resize((28, 28), Image.LANCZOS),
        dtype=np.float32
    )

    # 4) 0~1 범위로 정규화 (시각화용 이미지)
    display_image = img_resized / 255.0

    # 5) MNIST 정규화 적용 후 텐서로 변환
    normalized = (display_image - MNIST_MEAN) / MNIST_STD
    tensor = torch.FloatTensor(normalized).unsqueeze(0).unsqueeze(0)  # (1, 1, 28, 28)

    return tensor, display_image


def center_digit(img_array):
    """
    이미지에서 숫자를 찾아 중앙에 배치합니다.

    MNIST 데이터셋의 숫자는 28x28 이미지 안에서 약 20x20 크기로 중앙에 위치합니다.
    사용자가 캔버스 어디에 그리든 동일한 형태로 변환해야 정확도가 높아집니다.

    Args:
        img_array: numpy 배열 (280x280)

    Returns:
        중앙 정렬된 numpy 배열 (280x280)
    """
    # 비어있는 이미지 처리
    if img_array.max() == 0:
        return img_array

    # 숫자가 그려진 영역의 bounding box 찾기
    rows = np.any(img_array > 0, axis=1)
    cols = np.any(img_array > 0, axis=0)
    rmin, rmax = np.where(rows)[0][[0, -1]]
    cmin, cmax = np.where(cols)[0][[0, -1]]

    # 숫자 영역 crop
    digit = img_array[rmin:rmax + 1, cmin:cmax + 1]

    # MNIST 스타일: 숫자를 20x20 영역에 맞추고 28x28 중앙에 배치
    # 비율: 280px 캔버스 기준으로 200x200 영역에 맞춤
    h, w = digit.shape
    target_size = 200  # 280의 약 71% (28 중 20의 비율과 동일)

    # 비율 유지하면서 target_size에 맞춤
    scale = target_size / max(h, w)
    new_h = int(h * scale)
    new_w = int(w * scale)

    # PIL로 리사이즈 (LANCZOS 보간법: 고품질)
    digit_resized = np.array(
        Image.fromarray(digit.astype(np.uint8)).resize((new_w, new_h), Image.LANCZOS),
        dtype=np.float32
    )

    # 280x280 검은 이미지 중앙에 배치
    result = np.zeros((280, 280), dtype=np.float32)
    y_offset = (280 - new_h) // 2
    x_offset = (280 - new_w) // 2
    result[y_offset:y_offset + new_h, x_offset:x_offset + new_w] = digit_resized

    return result
