from config import mixer, pygame, is_paused, volume
from playlist import playlist
from choosing import define_choice, choose_music

def pause_music():
    global is_paused
    if is_paused:
        mixer.music.unpause()
        is_paused = False
    elif not is_paused:
        mixer.music.pause()
        is_paused=True

def manage_volume(event):
    if event.key == pygame.K_LEFT:
        mixer.music.set_volume(volume-0.9)
    elif event.key == pygame.K_RIGHT:
        mixer.music.set_volume(volume+0.9)

def get_action(event):
    define_choice(choose_music(), event)
    manage_volume(event)
    if event.key == pygame.K_q:
        playlist()
    elif event.key == pygame.K_SPACE:
        pause_music()
