import pygame
import sys
import random

pygame.init()
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 191, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


FPS = 60
clock = pygame.time.Clock()

gravity = 0.5
bird_movement = 0
bird = pygame.Rect(100, 300, 30, 30)

pipe_width = 60
pipe_gap = 150
pipe_speed = 4

pipes = []

def create_pipe():
    pipe_height = random.randint(1000, 400)
    top_pipe = pygame.Rect(SCREEN_WIDTH, pipe_height - pipe_gap - pipe_width, pipe_width, pipe_height)
    bottom_pipe = pygame.Rect(SCREEN_WIDTH, pipe_height, pipe_width, SCREEN_HEIGHT - pipe_height)
    return top_pipe, bottom_pipe
 
def move_pipes(pipes):
    for pipe in pipes:
        pipe.x -= pipe_speed
    return [pipe for pipe in pipes if pipe.x > -pipe_width]

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= SCREEN_HEIGHT:
            pygame.draw.rect(game_screen, GREEN, pipe)
        else:
            pygame.draw.rect(game_screen, RED, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird.colliderect(pipe):
            return False
    if bird.top <= 0 or bird.bottom >= SCREEN_HEIGHT:
        return False
    return True

def display_score(score):
    font = pygame.font.Font(None, 50)
    score_surface = font.render(f"Score: {score}", True, BLACK)
    game_screen.blit(score_surface, (10, 10))

# Game Loop hai Yha

running = True
pipes.extend(create_pipe())
score = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 8

    # Background game ka
    game_screen.fill(BLUE)

    # boll
    bird_movement += gravity
    bird.y += bird_movement
    pygame.draw.ellipse(game_screen, WHITE, bird)

    if not pipes or pipes[-1].x < SCREEN_WIDTH - 200:
        pipes.extend(create_pipe())

    pipes = move_pipes(pipes)
    draw_pipes(pipes)
    running = check_collision(pipes)
    for pipe in pipes:
        if pipe.centerx == bird.centerx:
            score += 1

    display_score(score)
    pygame.display.update()
    clock.tick(FPS)
