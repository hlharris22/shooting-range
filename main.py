import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

wood_bg = pygame.image.load("shooting+range+assets/shooting range assets/Wood_BG.png")
land_bg = pygame.image.load("shooting+range+assets/shooting range assets/Land_BG.png")
water_bg = pygame.image.load("shooting+range+assets/shooting range assets/Water_BG.png")
cloud_1 = pygame.image.load("shooting+range+assets/shooting range assets/Cloud1.png")
cloud_2 = pygame.image.load("shooting+range+assets/shooting range assets/Cloud2.png")

land_position_y = 560
land_speed = 1

water_position_y = 640
water_speed = 1.25

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(wood_bg, (0, 0))

    land_position_y -= land_speed
    if 520 >= land_position_y or 610 <= land_position_y:
        land_speed *= -1
    screen.blit(land_bg, (0, land_position_y))

    water_position_y -= water_speed
    if 575 >= water_position_y or 660 <= water_position_y:
        water_speed *= -1
    screen.blit(water_bg, (0, water_position_y))

    screen.blit(cloud_1, (600, 50))
    screen.blit(cloud_1, (1000, 75))
    screen.blit(cloud_1, (300, 15))
    screen.blit(cloud_2, (900, 55))
    screen.blit(cloud_2, (100, 10))
    screen.blit(cloud_2, (500, 100))
    pygame.display.update()
    clock.tick(120)