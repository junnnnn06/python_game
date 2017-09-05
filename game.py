# -*- coding:utf-8 -*-
import pygame
from pygame.locals import QUIT
import sys

pygame.init()                                   # Pygameの初期化
SURFACE = pygame.display.set_mode((400, 300))    # 大きさ400*300の画面を生成
pygame.display.set_caption("Just Window")              # タイトルバーに表示する文字

def main():
    while (1):
        SURFACE.fill((255,255,255))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了(画面閉じられる)
                sys.exit()

if __name__ == "__main__":
    main()
