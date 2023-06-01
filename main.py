from pygame import mixer
import pygame, sys, os
from playlist import playlist

pygame.init()
mixer.init()
directory = 'music/'

font = pygame.font.SysFont('Comic Sans', 30)
white = (255,255,255)

window = pygame.display.set_mode((500, 500))
is_paused = False
volume = mixer.music.get_volume()

def choose_music():
    songs=[i for i in os.listdir(directory)]
    count =0
    for n, song in enumerate(songs):
        text = font.render(f'{n+1}: {song}', False, white)
        count += 30
        window.blit(text, (0, count))
    return songs

def play_music(song):
    mixer.music.load(song)
    mixer.music.queue(song)
    mixer.music.play()

def define_choice(songs):
    keys = pygame.key.get_pressed()
    for key_constant, pressed in enumerate(keys):
        if pressed and key_constant-30 < len(songs) :
            choice = key_constant-30
            song = os.path.join(directory, songs[choice])
            play_music(song)
            break

def pause_music():
    global is_paused
    if is_paused:
        mixer.music.unpause()
        is_paused = False
    elif not is_paused:
        mixer.music.pause()
        is_paused=True

def manage_volume(event):
    if event == pygame.K_LEFT:
        mixer.music.set_volume(volume-0.9)
    elif event == pygame.K_RIGHT:
        mixer.music.set_volume(volume+0.9)

def get_action(event):
    manage_volume(event)
    if event == pygame.K_q:
        playlist(directory)
    elif event == pygame.K_SPACE:
        pause_music()

def close(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

def start():
    while True:
        for event in pygame.event.get():
            close(event)
            if event.type == pygame.KEYDOWN:
                get_action(event.key)

        define_choice(choose_music())
        pygame.display.update()

if '__main__'==__name__:
    start()
