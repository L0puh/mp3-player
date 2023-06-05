from choosing import choose_music
from config import pygame
import sys, actions


def close(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

def start():
    while True:
        for event in pygame.event.get():
            close(event)
            if event.type == pygame.KEYDOWN:
                actions.get_action(event)
        choose_music()
        pygame.display.update()

if '__main__'==__name__:
    start()
