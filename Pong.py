#PONG
import pygame, sys, random

#Gerneral
pygame.init()
clock = pygame.time.Clock()

#Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960
RECT_COLOR = (93, 93, 134)
BG_COLOR = (6, 6, 44)
BALL_SPEED_X = 7 * random.choice((1, -1))
BALL_SPEED_Y = 7 * random.choice((1, -1))
PLAYER_SPEED = 0
OPPONENT_SPEED = 7
LINE_WIDTH = 2


#Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PONG")

#Objects
ball = pygame.Rect(SCREEN_WIDTH / 2 - 15, SCREEN_HEIGHT / 2 - 15, 30, 30)
player = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT / 2 - 70, 10,140)
opponent = pygame.Rect(10, SCREEN_HEIGHT / 2 - 70, 10,140)

#Functions
def draw():
    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, RECT_COLOR, player)
    pygame.draw.rect(screen, RECT_COLOR, opponent)
    pygame.draw.ellipse(screen, RECT_COLOR, ball)
    pygame.draw.line(screen, RECT_COLOR, (SCREEN_WIDTH /2, 0), (SCREEN_WIDTH /2, SCREEN_HEIGHT), LINE_WIDTH)
def ball_movement():
    global BALL_SPEED_X, BALL_SPEED_Y

    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y

    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        BALL_SPEED_Y *= -1
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        resart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        BALL_SPEED_X *= -1
def player_movement():
    player.y += PLAYER_SPEED
    if player.top <= 0:
        player.top = 0
    if player.bottom >= SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT
def opponent_movement():
    if opponent.top < ball.y:
        opponent.top += OPPONENT_SPEED
    if opponent.bottom > ball.y:
        opponent.bottom -= OPPONENT_SPEED
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= SCREEN_HEIGHT:
        opponent.bottom = SCREEN_HEIGHT
def resart():
    global BALL_SPEED_X, BALL_SPEED_Y
    ball.center = (SCREEN_WIDTH /2, SCREEN_HEIGHT/2)
    BALL_SPEED_X *= random.choice((1, -1))
    BALL_SPEED_Y *= random.choice((1, -1))

#Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                PLAYER_SPEED += 7
            if event.key == pygame.K_UP:
                PLAYER_SPEED -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                PLAYER_SPEED -= 7
            if event.key == pygame.K_UP:
                PLAYER_SPEED += 7


    ball_movement()
    player_movement()
    opponent_movement()
    draw()

    pygame.display.update()
    clock.tick(60)