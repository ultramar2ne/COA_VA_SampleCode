""" cave - Copyright 2016 Kenchiro Tanaka"""
import sys
from random import randint
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE

pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((800, 600))
FPSCLOCK = pygame.time.Clock()


def main():
    """ main Routine"""
    walls = 80
    ship_y = 250
    velocity = 0
    score = 0
    slope =randint(1, 6)
    sysfont = pygame.font.SysFont(None, 36)
    ship_image = pygame.image.load("airplane.png")
    bang_image = pygame.image.load("C:\\Users\\owl06\\PycharmProjects\\back\\venv\\Lib\\site-packages\\pygame"
                                   "\\examples\\data\\explosion1.gif")
    holes = []
    for xpos in range(walls):
        holes.append(Rect(xpos*10, 100, 10, 400))
    game_over = False
    while True:
        is_space_down = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    is_space_down = True

        if not game_over:
            score += 10
            velocity += -3 if is_space_down else 3
            ship_y += velocity

            edge = holes[-1].copy()
            test = edge.move(0, slope)
            if test.top <= 0 or test.bottom >= 600:
                slope = randint(1, 6) * (-1 if slope > 0 else 1)
                edge.inflate_ip(0, -20)
            edge.move_ip(10, slope)
            holes.append(edge)
            del holes[0]
            holes =[x.move(-10, 0) for x in holes]
            if holes[0].top > ship_y or holes[0].bottom < ship_y + 40:
                game_over = True

        SURFACE.fill((0, 255, 0))
        for hole in holes:
            pygame.draw.rect(SURFACE, (0, 0, 0), hole)
        SURFACE.blit(ship_image, (0, ship_y))
        score_image = sysfont.render("Score is {}".format(score), True, (0, 0, 255))
        SURFACE.blit(score_image, (600, 20))

        if game_over:
            SURFACE.blit(bang_image, (0, ship_y-40))
        pygame.display.update()
        FPSCLOCK.tick(15)


if __name__ == "__main__":
    main()