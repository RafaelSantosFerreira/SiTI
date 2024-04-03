#ffmpeg -f rawvideo -pix_fmt yuv420p -s 3840x2160 -r 30 -i /home/gaci/videos/4K/Campfire_3840x2160_30fps_bt709_420_videoRange.yuv -vf "fps=1" quadro_%04d.png

import cv2
import numpy as np
import os
import argparse
from concurrent.futures import ProcessPoolExecutor

# Argumentos de linha de comando
parser = argparse.ArgumentParser(description='Calcula SI e TI de um vídeo.')
parser.add_argument('diretorio', type=str, help='Diretório contendo os quadros do vídeo.')
args = parser.parse_args()

def calcular_si(quadro_nome):
    quadro = cv2.imread(quadro_nome, cv2.IMREAD_GRAYSCALE)
    sobelx = cv2.Sobel(quadro, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(quadro, cv2.CV_64F, 0, 1, ksize=3)
    magnitude = np.sqrt(sobelx**2 + sobely**2)
    si = np.var(magnitude)
    return si

def calcular_ti(quadros):
    quadro1 = cv2.imread(quadros[0], cv2.IMREAD_GRAYSCALE)
    quadro2 = cv2.imread(quadros[1], cv2.IMREAD_GRAYSCALE)
    diferenca = cv2.absdiff(quadro1, quadro2)
    ti = np.mean(diferenca)
    return ti

def main(diretorio):
    quadros = sorted([os.path.join(diretorio, f) for f in os.listdir(diretorio) if f.startswith('quadro_') and f.endswith('.png')])
    with ProcessPoolExecutor() as executor:
        si_valores = list(executor.map(calcular_si, quadros))
        ti_valores = list(executor.map(calcular_ti, zip(quadros, quadros[1:])))
    
    print(f'Informação Espacial (SI): {np.mean(si_valores)}')
    print(f'Informação Temporal (TI): {np.mean(ti_valores)}')

if __name__ == "__main__":
    main(args.diretorio)
