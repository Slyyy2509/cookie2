import os
import cv2
import albumentations as A
from albumentations import Compose, HorizontalFlip, VerticalFlip, Rotate

OUTPUT_DIR = "screenshots"
os.makedirs(OUTPUT_DIR, exist_ok=True)

augmentation = A.Compose([
    # Изменение яркости и контрастности (от 0.8 до 1.2)
    A.RandomBrightnessContrast(brightness_limit=(-0.2, 0.2), contrast_limit=(-0.3, 0.3)),
    
    # Сдвиг изображения по осям X и Y на ±5%
    A.ShiftScaleRotate(
        shift_limit_x=(-0.05, 0.05),
        shift_limit_y=(-0.05, 0.05),
        rotate_limit=(-4, 4),
        p=0.3,
    ),
    
    # Масштабирование: от -10% до +10%, поворот — ±7°
    A.Affine(scale=(0.9, 1.1), translate_percent=(-0.1, 0.1), p=0.3),
    
    # Перспективные искажения (±10%)
    A.Perspective(scale=(0.08, 0.12), p=0.3),
    
    # Отражение по горизонтали или вертикали
    A.OneOf([A.HorizontalFlip(p=0.5), A.VerticalFlip(p=0.5)], p=0.5),
])

image_extensions = [".jpg", ".jpeg", ".png", ".webp"]
for idx, file in enumerate(listdir):
    img_path = os.path.join(DATASET_DIR, file)
    if Path(img_path).suffix in image_extensions:
        img_name = Path(file).stem[:3]
        img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
        
        for i in range(AUGMENTATION_TIMES):
            transformed = augmentation(image=img)
            
            # Сохраняем в формате RGB
            r, g, b, a = cv2.split(transformed["image"])
            output_img = cv2.merge((b, g, r, a))

            out_file = f"{idx}_{i:03d}{Path(file).suffix}"
            out_path = os.path.join(OUTPUT_DIR, out_file)

            print(f"Генерируется изображение: {out_file} ({i+1}/{len(listdir)*AUGMENTATION_TIMES})")