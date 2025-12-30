import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game window
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Clock and snake settings
clock = pygame.time.Clock()
snake_block = 20
snake_speed = 10

# Font
font = pygame.font.SysFont(None, 35)

def draw_text(text, color, x, y):
    msg = font.render(text, True, color)
    win.blit(msg, [x, y])

def game_loop():
    game_over = False
    game_close = False

    x = WIDTH // 2
    y = HEIGHT // 2
    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    food_x = random.randrange(0, WIDTH - snake_block, snake_block)
    food_y = random.randrange(0, HEIGHT - snake_block, snake_block)

    while not game_over:

        while game_close:
            win.fill(BLACK)
            draw_text("Game Over! Press C-Play Again or Q-Quit", RED, 40, HEIGHT // 2)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += x_change
        y += y_change
        win.fill(BLACK)
        pygame.draw.rect(win, RED, [food_x, food_y, snake_block, snake_block])
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for part in snake_list[:-1]:
            if part == snake_head:
                game_close = True

        for part in snake_list:
            pygame.draw.rect(win, GREEN, [part[0], part[1], snake_block, snake_block])

        draw_text(f"Score: {snake_length - 1}", WHITE, 10, 10)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH - snake_block, snake_block)
            food_y = random.randrange(0, HEIGHT - snake_block, snake_block)
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()

game_loop()
