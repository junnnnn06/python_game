import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock()

def main():
    logo = pygame.image.load('/Users/JUN/python.jpg')
    theta = 0
    while True:
        for event in pygame.event.get(QUIT):
            pygame.quit()
            sys.exit()
        theta += 1

        SURFACE.fill((225,225,225))
        new_logo = pygame.transform.rotate(logo, theta)
        rect = new_logo.get_rect()
        rect.center = (200,150)
        SURFACE.blit(new_logo, rect)
        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()

# Surface.get_rect
# Surfaceが存在する範囲のRect値を取得します。
# Surfaceが存在する範囲全体をRect値の戻り値として返します。
# このRect型範囲は常に(0,0)座標を起点とし、
# 幅と高さはそれぞれSurface全体に表示される画像と同じものとなります。
# この命令ではキーワードとその値を引数として設定することができます。
# このキーワード値がRect型クラスの該当する値に設定されたうえで、
# 戻り値が返ります。例えば、'get_rect(center=(100,100))'という引数を設定した場合、
# Surfaceの中心が(100,100)座標となった状態のRect値が取得されます。
