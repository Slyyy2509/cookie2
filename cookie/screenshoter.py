
from mss import mss # Быстрая библиотека для скринов
from datetime import datetime
import os
import time

# Для сохранения файла нужен модуль Image из Pillow
from PIL import Image

save_dir = "screenshots"
os.makedirs(save_dir, exist_ok=True)

print("Начинаем делать скриншоты каждые 5 секунд...")
print("Нажмите ctrl+c для остановки")

count = 0
try:
    with mss() as sct: # Создаем контекстный менеджер для захвата экрана
        while True:
            # Делаем скриншот. Монитор=1 — это основной экран.
            screenshot = sct.grab(sct.monitors[1])
            
            timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
            filename = f"{save_dir}/screenshot_{timestamp}.png"

            # Преобразуем raw-данные от mss в формат PIL и сохраняем
            img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX") # BGRA -> RGB
            img.save(filename)

            count += 1
            print(f"[{count}] сохранено: {filename}")

            time.sleep(5) # Пауза между снимками
except KeyboardInterrupt:
    pass

print(f"Всего сделано скриншотов: ({count})")