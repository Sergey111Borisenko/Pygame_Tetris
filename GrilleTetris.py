import pygame

class GrilleT:
    def __init__(self):
        self.L = [pygame.image.load("ryan_gosling.jpg"),
             pygame.image.load("kaney_west.jpg"),
             pygame.image.load("mog_guy.jpg")]

        for i in range(len(self.L)):
            self.L[i] = pygame.transform.scale(self.L[i], (40, 40))

        self.colonnes = 10
        self.lignes = 20
        self.celluleTaille = 40
        self.grille = [[0 for j in range(self.colonnes)] for i in range(self.lignes)]

    def affiche_grille(self):
        for i in range(self.lignes):
            for j in range(self.colonnes):
                print(self.grille[i][j], end = " ")
            print()

    def dessine_grille(self, screen):
        for i in range(self.lignes):
            for j in range(self.colonnes):
                ValeurCellule = self.grille[i][j]
                screen.blit(self.L[ValeurCellule], (j * self.celluleTaille, i * self.celluleTaille))
