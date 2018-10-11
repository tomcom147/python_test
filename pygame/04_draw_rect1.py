""" draw_rect1.py """
import sys
import pygame
from pygame.locals import QUIT, Rect

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))
FPSCLOCK = pygame.time.Clock()

def main():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    SURFACE.fill((255, 255, 255))

    # 赤：矩形（塗りつぶし）
    pygame.draw.rect(SURFACE, (255, 0, 0), (10,20,100,50))
    #赤：矩形（太さ３）
    pygame.draw.rect(SURFACE, (255, 0, 0), (150, 10, 100, 30), 3)

    ##

    pygame.display.update()
    FPSCLOCK.tick(3)

if __name__ == "__main__":
    main()