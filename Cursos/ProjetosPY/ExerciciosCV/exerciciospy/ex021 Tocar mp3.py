import pygame

pygame.init()
pygame.mixer.music.load("Desafios\Módulo 1\Aula 8\Arquivos\ex021\kids-saying-yay-sound-effect_3.mp3")
pygame.mixer.music.play(loops=0)

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)