import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Tetris")
clock = pygame.time.Clock()

the_rock = pygame.image.load("the_rock_sitting.jpg")
the_rock = pygame.transform.scale(the_rock, (800, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(the_rock, (0, 0))
    pygame.display.update()
    clock.tick(60)