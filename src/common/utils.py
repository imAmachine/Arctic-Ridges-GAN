import json
import cv2
import numpy as np


class Utils:
    @staticmethod
    def binarize_by_threshold(image: np.ndarray, threshold: float=127.0, max_val: float=1.0):
        _, binary = cv2.threshold(image, threshold, max_val, cv2.THRESH_BINARY)
        return binary
    
    @staticmethod
    def cv2_load_image(filename: str, cv2_read_mode: int=None):
        if cv2_read_mode is None:
            img = cv2.imread(filename)
        else:
            img = cv2.imread(filename, cv2_read_mode)
        
        if img is None:
            raise ValueError(f"Failed to load image {filename}")
        
        return img
    
    @staticmethod
    def crop_image(img: np.ndarray, crop_percent: int = 0) -> np.ndarray:
        if crop_percent > 0:
            h, w = img.shape
            crop_size_w, crop_size_h = int(w * (crop_percent / 100)), int(h * (crop_percent / 100))
            return img[crop_size_w:w-crop_size_w, crop_size_h:h-crop_size_h]
        return img
    
    @staticmethod
    def check_binary_format(img: np.ndarray) -> bool:
        """
        Проверяет, что изображение является бинарным: содержит **только** значения 0 и 1.
        
        Args:
            img (np.ndarray): Изображение, представленное в виде массива.
        
        Returns:
            bool: True, если изображение бинарное, иначе False.
        """
        
        unique_values = np.unique(img)
        return np.array_equal(unique_values, [0]) or \
            np.array_equal(unique_values, [1]) or \
            np.array_equal(unique_values, [0, 1])
    
    @staticmethod
    def to_json(data, path):
        with open(path, 'w+', encoding='utf8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    
    @staticmethod
    def from_json(path):
        with open(path, 'r', encoding='utf8') as f:
            return json.load(f)