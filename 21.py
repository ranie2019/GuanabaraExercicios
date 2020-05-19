# Tocando um MP3

import pygame
pygame.init()
pygame.mixer_music.load('21.mp3')
pygame.mixer_music.play()
pygame.event.wait()