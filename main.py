import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("MinecraftNoah")
icon = pygame.image.load("img/avatar.png")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/zombi.png")
target_width = 80
target_height = 80

target_x = random.randint(0, screen_width - target_width)
target_y = random.randint(0, screen_height - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Score setup
score = 0
font = pygame.font.Font(None, 36)  # Use default font

running = True
while running:
    screen.fill(color)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, screen_width - target_width)
                target_y = random.randint(0, screen_height - target_height)
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Optional
                score += 1

    # Draw target
    screen.blit(target_img, (target_x, target_y))

    # Draw score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
