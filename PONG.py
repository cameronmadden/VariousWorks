import pygame
import random
import os

pygame.init()

WIDTH, HEIGHT = 1200, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
FPS = 60

P1Y = 30
P2Y = 30
def draw_window(p1, p2, circ_x, circ_y, score1, score2):
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, RED, (30, p1.y, 60, 180))
    pygame.draw.rect(WIN, BLUE, (1110, p2.y, 60, 180))
    pygame.draw.circle(WIN, WHITE, (circ_x, circ_y), 30)

    scoreFont = pygame.font.SysFont('comicsans', 32)
    draw_score_1 = scoreFont.render(str(score1), 1, WHITE)
    draw_score_2 = scoreFont.render(str(score2), 1, WHITE)
    WIN.blit(draw_score_1, (100, 100))
    WIN.blit(draw_score_2, (1100, 100))
    pygame.display.update()


def main():

    score1 = 0
    score2 = 0

    p1 = pygame.Rect(30, 360, 60, 180)
    p2 = pygame.Rect(1110, 360, 60, 180)

    circ_x = 600
    circ_y = 450

    speed = 5
    circ_x_vel = speed
    circ_y_vel = 0

    circ_x_dir = 1
    circ_y_dir = 1

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_DOWN]:
            p2.y += 5
        if keys_pressed[pygame.K_UP]:
            p2.y -= 5
        if keys_pressed[pygame.K_s]:
            p1.y += 5
        if keys_pressed[pygame.K_w]:
            p1.y -= 5

        circ_x += circ_x_vel
        circ_y += circ_y_vel
        if circ_x + 30 >= 1110 and circ_y + 30 > p2.y and circ_y - 30 < p2.y + 180:

            speed += 1
            xdiff = abs(circ_x - (p2.x + 15))
            ydiff = (circ_y - (p2.y + 90))

            hyp = (xdiff**2 + abs(ydiff)**2)**0.5

            circ_x_vel = - (xdiff/hyp) * speed
            circ_y_vel = (ydiff/hyp) * speed

        if circ_x - 30 <= 90 and circ_y + 30 > p1.y and circ_y - 30 < p1.y + 180:
            circ_x_dir = 1
            speed += 1
            xdiff = abs(circ_x - (p1.x + 15))
            ydiff = (circ_y - (p1.y + 90))

            hyp = (xdiff ** 2 + abs(ydiff) ** 2) ** 0.5

            circ_x_vel = (xdiff / hyp) * speed
            circ_y_vel = (ydiff / hyp) * speed

        if circ_x + 30 >= 1200:
            score1 += 1

            speed = 5
            circ_x_vel = speed
            circ_y_vel = 0

            circ_x = 600
            circ_y = 400

        if circ_x - 30 <= 0:
            score2 += 1

            speed = 5
            circ_x_vel = circ_x_vel * speed/abs(circ_x_vel)
            circ_y_vel = 0

            circ_x = 600
            circ_y = 400

        if circ_y + 30 >= 900 or circ_y - 30 <= 0:
            circ_y_vel *= -1
        draw_window(p1, p2, circ_x, circ_y, score1, score2)

    pygame.quit()


if __name__ == "__main__":
    main()
