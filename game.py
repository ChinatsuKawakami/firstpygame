#project folder name : pygame
#file name : game
#Author : Chinatsu Kawakami
#Description: this is my first pygame project
#Date 22 July 2017
#version : 0.0.1

import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashd = True
    print(event)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()