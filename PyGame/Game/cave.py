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

            edge = holes[-1].copy()  # 가장오른쪽에 있는 Rect을 copy함
            test = edge.move(0, slope)  # SLope 값만큼 이동
            if test.top <= 0 or test.bottom >= 600:
                slope = randint(1, 6) * (-1 if slope > 0 else 1)  # 부딫혔을때 방향바꿈
                edge.inflate_ip(0, -20)  # Size를 변경함
            edge.move_ip(10, slope)
            holes.append(edge)  # 위치가 변경된 edge를 리스트에 더해줌
            del holes[0]  # 가장 왼쪽 Rect 삭제
            holes = [x.move(-10, 0) for x in holes]  # 전체 Holes를 왼쪽을 10만큼 이동
            if holes[0].top > ship_y or holes[0].bottom < ship_y + 40:
                game_over = True

        SURFACE.fill((0, 255, 0))  # 기본 색이 초록이다.
        for hole in holes:
            pygame.draw.rect(SURFACE, (0, 0, 0), hole)  # 초록 바탕에다가 검정색 사각형을 그리기
        SURFACE.blit(ship_image, (0, ship_y))
        score_image = sysfont.render("Score is {}".format(score), True, (0, 0, 255))
        SURFACE.blit(score_image, (600, 20))

        if game_over:
            SURFACE.blit(bang_image, (0, ship_y-40))
        pygame.display.update()
        FPSCLOCK.tick(15)


if __name__ == "__main__":
    main()