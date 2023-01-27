import sys

import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

wood_bg = pygame.image.load("shooting+range+assets/shooting range assets/Wood_BG.png")
land_bg = pygame.image.load("shooting+range+assets/shooting range assets/Land_BG.png")
water_bg = pygame.image.load("shooting+range+assets/shooting range assets/Water_BG.png")
cloud_1 = pygame.image.load("shooting+range+assets/shooting range assets/Cloud1.png")
cloud_2 = pygame.image.load("shooting+range+assets/shooting range assets/Cloud2.png")
crosshair = pygame.image.load("shooting+range+assets/shooting range assets/crosshair.png")
duck_surface = pygame.image.load("shooting+range+assets/shooting range assets/duck.png")

land_position_y = 560
land_speed = 1

water_position_y = 640
water_speed = 1.25

crosshair_rect = crosshair.get_rect(center=(640, 360))

duck_list = []
for duck in range(0, 20):
    duck_position_x = random.randrange(50, 1200)
    duck_position_y = random.randrange(160, 600)
    duck_rect = duck_surface.get_rect(center=(duck_position_x, duck_position_y))
    duck_list.append(duck_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair.get_rect(center=event.pos)
    screen.blit(wood_bg, (0, 0))

    land_position_y -= land_speed
    if land_position_y <= 520 or land_position_y >= 610:
        land_speed *= -1
    screen.blit(land_bg, (0, land_position_y))
    for duck_rect in duck_list:
        screen.blit(duck_surface, duck_rect)
    water_position_y -= water_speed
    if water_position_y <= 575 or water_position_y >= 660:
        water_speed *= -1
    screen.blit(water_bg, (0, water_position_y))

    screen.blit(crosshair, crosshair_rect)

    screen.blit(cloud_1, (600, 50))
    screen.blit(cloud_1, (1000, 75))
    screen.blit(cloud_1, (300, 15))
    screen.blit(cloud_2, (900, 55))
    screen.blit(cloud_2, (100, 10))
    screen.blit(cloud_2, (500, 100))
    pygame.display.update()
    clock.tick(120)
