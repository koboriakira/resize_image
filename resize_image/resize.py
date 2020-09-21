import cv2
import numpy as np


def resize(file_path: str):
    img: np.ndarray = cv2.imread(file_path)
    width: int = len(img[0])
    height: int = len(img)

    # 16:9になっているかを確認
    result = (width * 9) / (height * 16)
    if result == 0:
        print('正しい比率です')
        return
    elif result > 0:
        # 正しい幅、高さを計算
        correct_width: int = int((height * (16 / 9)))
        new_img = cv2.resize(img, (correct_width, height))
        cv2.imwrite(f'{file_path}-resize.png', new_img)
    elif result < 0:
        # 正しい幅、高さを計算
        correct_height: int = int((width * (9 / 16)))
        new_img = cv2.resize(img, (width, correct_height))
        cv2.imwrite(f'{file_path}-resize.png', new_img)
