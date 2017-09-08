import sys
import pygame
from pygame.locals import QUIT, Rect

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))
FPSCLOCK = pygame.time.Clock()

def main():
    sysfont = pygame.font.SysFont(None, 36)
    counter = 0
    while True:
        for event in pygame.event.get(QUIT):
            pygame.quit()
            sys.exit()

        SURFACE.fill((0,0,0))
        #赤:短形
        pygame.draw.ellipse(SURFACE,(255, 0, 0), (40,20,140,60), 10)
        #赤:短形
        pygame.draw.line(SURFACE,(255,0,0),(50,50),(200,50), 5)
        #緑:短形
        pygame.draw.circle(SURFACE, (0,255,0),(150,150), 20)
        #青:短形、Rectオブジェクト
        rect0 = Rect(200, 60, 140, 80)
        pygame.draw.rect(SURFACE, (0,0,255), rect0)
        #格子
        for xpos in range(0,400,25):
            pygame.draw.line(SURFACE, 0xFFFFFF,(xpos,0),(xpos,300))
        for ypos in range(0,300,25):
            pygame.draw.line(SURFACE, 0xFFFFFF,(0,ypos),(400,ypos))
        pygame.display.update()
        FPSCLOCK.tick(3)
if __name__ == "__main__":
    main()
