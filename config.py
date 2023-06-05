import pygame
from pygame import mixer

pygame.init()
mixer.init()
directory = 'music/'

font = pygame.font.SysFont('Comic Sans', 30)
white = (255,255,255)
black = (0,0,0)

window = pygame.display.set_mode((500, 500))
is_paused = False
volume = mixer.music.get_volume()
