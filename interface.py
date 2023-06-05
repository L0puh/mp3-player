import pygame
from config import window, font, white

def print_text(text, pos, *fill):
    if fill:
        window.fill(fill)
    t = font.render(text, False, white)
    window.blit(t, pos)
