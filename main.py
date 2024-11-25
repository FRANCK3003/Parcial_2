from botones import *
import pygame

# Inicializamos pygame Y el mixer

pygame.mixer.init()



# MUSICA
musica = pygame.mixer.music.load("JUEGO_EN_CONJUNTO/assets/Toxicity.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.05)


menu()
