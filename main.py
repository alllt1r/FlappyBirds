import pygame
import sys
import random
import time

FPS = 60
WIN_WIDTH = 700
WIN_HEIGHT = 500
WHITE = 255, 255, 255
BLACK = 0, 0, 0
jump_count = 15
jump = False
x = 150
y = WIN_HEIGHT // 2
start_x = 175
start_y = 80
quit_x = 175
quit_y = 200
retry_x = 175
retry_y = 80
wall_x = 710
wall_x1 = 1100
wall_x2 = 1390
wall_y = random.randrange(-1450, -1170)
wall_y1 = random.randrange(-1450, -1170)
wall_y2 = random.randrange(-1450, -1170)
gr_x = 0
gr_y = 0
gr1_x = 700
gr1_y = 0
bird_count = 0
angle = 0
draw = True
die = False
scores = 0
c = 0
high_scores = 21 * 15

pygame.init()
clock = pygame.time.Clock()
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
ip = 'images/'
pygame.display.set_caption(ip + 'Flappy Birds')
#icon = pygame.image.load(ip + 'icon.png')
#pygame.display.set_icon(icon)
wall = pygame.image.load(ip + 'Wall.png')
a = pygame.transform.rotate(pygame.image.load(ip + 'bird 1.png'), angle)
b = pygame.transform.rotate(pygame.image.load(ip + 'bird 2.png'), angle)
start_game_UI = pygame.image.load(ip + 'Start_game_UI.png')
start_game_1_UI = pygame.image.load(ip + 'Start_game_1_UI.png')
quit_UI = pygame.image.load(ip + 'Quit_UI.png')
quit_1_UI = pygame.image.load(ip + 'Quit_1_UI.png')
Retry_UI = pygame.image.load(ip + 'RETRY_UI.png')
Retry_1_UI = pygame.image.load(ip + 'RETRY_1_UI.png')
ground = pygame.image.load(ip + 'ground.png')
bird_img = [a, b]


def draw_UI_1():
    global retry_x, retry_y, Retry_1_UI, Retry_UI, quit_x, quit_y, quit_1_UI, quit_UI, game, wall_x, wall_x1, wall_x2, scores, x, c, y, angle
    mouse = pygame.mouse.get_pos()

    if c == 1:
        pygame.mixer.music.load(ip + 'sfx_die.wav')
        pygame.mixer.music.play(1)
    c = 0
    if 174 < mouse[0] < 525 and 79 < mouse[1] < 181:
        sc.blit(Retry_1_UI, (retry_x, retry_y))
        if pygame.mouse.get_pressed() == (1, 0, 0):
            wall_x = 710
            wall_x1 = 1100
            wall_x2 = 1300
            y = 200
            angle = 0
            scores = 0
            game = True
    else:
        sc.blit(Retry_UI, (retry_x, retry_y))
    if 174 < mouse[0] < 525 and 199 < mouse[1] < 301:
        sc.blit(quit_1_UI, (quit_x, quit_y))
        if pygame.mouse.get_pressed() == (1, 0, 0):
            pygame.quit()
            sys.exit()
    else:
        sc.blit(quit_UI, (quit_x, quit_y))
    pygame.display.update()
    clock.tick(FPS)


def print_text(message, ax, ay, font_color=BLACK, font_type=ip + '18888.ttf', font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    sc.blit(text, (ax, ay))


def make_jump():
    global y, jump_count, jump
    if jump_count >= 0:
        y -= jump_count  # / 3
        jump_count -= 1
    else:
        jump_count = 15
        jump = False


def bird_draw():
    global bird_count, x, y, bird_img
    if bird_count == 8:
        bird_count = 0
    sc.blit(bird_img[bird_count // 4], (x, y))
    bird_count += 1
    bird_img = [a, b]


def wall1_draw():
    global wall_y, wall_x, wall_x1, y, die, game, scores, c
    sc.blit(wall, (wall_x, wall_y))
    if wall_x >= -249:
        wall_x -= 5
    if wall_x <= -250:
        wall_x = 710
        wall_y = random.randrange(-1450, -1170)
    if 0 < wall_x < 80 and (y > wall_y + 1625 or y < wall_y + 1470):
        game = False
        c = 1
    if 0 < wall_x < 80 and (y < wall_y + 1625 or y > wall_y + 1470):
        if scores % 15 == 0:
            pygame.mixer.music.load(ip + 'Point.mp3')
            pygame.mixer.music.play(1)
        scores += 1


def wall2_draw():
    global wall_y1, wall_x1, game, scores, c
    sc.blit(wall, (wall_x1, wall_y1))
    if wall_x1 >= -249:
        wall_x1 -= 5
    if wall_x1 <= -250:
        wall_x1 = 710
        wall_y1 = random.randrange(-1450, -1170)
    if 0 < wall_x1 < 80 and (y > wall_y1 + 1625 or y < wall_y1 + 1470):
        game = False
        c = 1
    if 0 < wall_x1 < 80 and (y < wall_y1 + 1625 or y > wall_y1 + 1470):
        if scores % 15 == 0:
            pygame.mixer.music.load(ip + 'Point.mp3')
            pygame.mixer.music.play(1)
        scores += 1


def wall3_draw():
    global wall_y2, wall_x2, game, scores, c
    sc.blit(wall, (wall_x2, wall_y2))
    if wall_x2 >= -249:
        wall_x2 -= 5
    if wall_x2 <= -250:
        wall_x2 = 710
        wall_y2 = random.randrange(-1450, -1170)
    if 0 < wall_x2 < 80 and (y > wall_y2 + 1625 or y < wall_y2 + 1470):
        game = False
        c = 1
    if 0 < wall_x2 < 80 and (y < wall_y2 + 1625 or y > wall_y2 + 1470):
        if scores % 15 == 0:
            pygame.mixer.music.load(ip + 'Point.mp3')
            pygame.mixer.music.play(1)
        scores += 1


def scores1():
    global scores, high_scores
    if scores > high_scores:
        high_scores = scores
    print_text('Scores: ' + str(scores // 15), 10, 10)
    print_text('High Scores: ' + str(high_scores // 15), 10, 50)


def draw_ground():
    global gr_x, gr_y, gr1_x, gr1_y
    sc.blit(ground, (gr_x, gr_y))
    sc.blit(ground, (gr1_x, gr1_y))
    if gr_x > -699:
        gr_x -= 5
    else:
        gr_x = 699
    if gr1_x > -699:
        gr1_x -= 5
    else:
        gr1_x = 699


game = True
while True:
    for err in pygame.event.get():
        if err.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if game == True:
        if draw == False:
            sc.fill(WHITE)
            # draw_ground()
            bird_draw()
            wall1_draw()
            wall2_draw()
            wall3_draw()
            keys = pygame.key.get_pressed()
            if y >= 25:
                if keys[pygame.K_SPACE]:
                    jump = True
            if jump:
                make_jump()
            else:
                y += 7
                pass
            if angle >= -90:
                a = pygame.transform.rotate(pygame.image.load(ip + 'bird 1.png'), angle)
                b = pygame.transform.rotate(pygame.image.load(ip + 'bird 2.png'), angle)
                angle -= 5
            if keys[pygame.K_SPACE]:
                while angle < 50:
                    angle += 5
            if y >= 500:
                c = 1
                game = False
                draw_UI_1()
            if die == True:
                game = False

        else:
            mouse = pygame.mouse.get_pos()
            if 174 < mouse[0] < 525 and 79 < mouse[1] < 181:
                sc.blit(start_game_1_UI, (start_x, start_y))
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    draw = False
            else:
                sc.blit(start_game_UI, (start_x, start_y))
            if 174 < mouse[0] < 525 and 199 < mouse[1] < 301:
                sc.blit(quit_1_UI, (quit_x, quit_y))
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    pygame.quit()
                    sys.exit()
            else:
                sc.blit(quit_UI, (quit_x, quit_y))
    if game == False:
        draw_UI_1()
    scores1()
    pygame.display.update()
    clock.tick(FPS) 