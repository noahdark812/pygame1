import pygame
import random
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("MinecraftNoah")
icon = pygame.image.load("img/Minecraft-creeper-face.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/zombi1.png")
target_width = 80
target_height = 80

target_x = random.randint(0, screen_width - target_width)
target_y = random.randint(0, screen_height - target_height)

color = (random.randint(0, 255),random.randint(0, 255), random.randint(0,255))



running = True
while running:
    pass

pygame.quit()

