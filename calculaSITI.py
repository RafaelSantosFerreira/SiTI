#ffmpeg -f rawvideo -pix_fmt yuv420p -s 3840x2160 -r 30 -i /home/gaci/videos/4K/Campfire_3840x2160_30fps_bt709_420_videoRange.yuv -vf "fps=1" quadro_%04d.png

import cv2
import numpy as np
import os

quadros = sorted([f for f in os.listdir('.') if f.startswith('quadro_') and f.endswith('.png')])
diferencas = []

for i in range(1, len(quadros)):
    quadro1 = cv2.imread(quadros[i-1], cv2.IMREAD_GRAYSCALE)
    quadro2 = cv2.imread(quadros[i], cv2.IMREAD_GRAYSCALE)
    diferenca = cv2.absdiff(quadro1, quadro2)
    media = np.mean(diferenca)
    diferencas.append(media)

ti = np.mean(diferencas)
print(f'Informacao Temporal (TI): {ti}')
