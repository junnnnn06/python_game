import sys
import pygame
from pygame.locals import QUIT,\
      KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN

SCREEN_SIZE = (400,300)

pygame.init()
pygame.key.set_repeat(5,5)
SURFACE = pygame.display.set_mode(SCREEN_SIZE)
FPSCLOCK = pygame.time.Clock()

def main():
    logo = pygame.image.load("/Users/JUN/python.jpg")
    pos = [200,150]
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN or event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pos[0] -= 5
                elif event.key == pygame.K_RIGHT:
                    pos[0] += 5
                elif event.key == pygame.K_UP:
                    pos[1] -= 5
                elif event.key == pygame.K_DOWN:
                    pos[1] += 5

        pos[0] = pos[0] % 400
        pos[1] = pos[1] % 300

        SURFACE.fill((255,255,255))
        rect = logo.get_rect()
        rect.center = pos
        SURFACE.blit(logo, rect)
        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()
