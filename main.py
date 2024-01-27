from GrilleTetris import GrilleT

import pygame
import sys

#pygame
pygame.init()
screen = pygame.display.set_mode((450, 850))
pygame.display.set_caption("Pygame Tetris")
clock = pygame.time.Clock()

the_rock = pygame.image.load("the_rock_sitting.jpg")
the_rock = pygame.transform.scale(the_rock, (450, 850))
screen.blit(the_rock, (0, 0))

#Grille Tetris
grilleThis = GrilleT()
grilleThis.affiche_grille()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    grilleThis.dessine_grille(screen)
    pygame.display.update()
    clock.tick(60)