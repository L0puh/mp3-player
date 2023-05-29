from pygame import mixer
import os

mixer.init()
directory = 'music/'

is_paused = False
volume = mixer.music.get_volume()


def choose_music():
    songs=[i for i in os.listdir(directory)]
    [print(f'{n+1}: {song}') for n, song in enumerate(songs)]
    choice = songs[int(input())-1]
    mixer.music.load(os.path.join(directory, choice))
    mixer.music.play()

def pause_music(action):
    global is_paused
    if is_paused and action=='p':
        mixer.music.unpause()
        is_paused = False
    elif not is_paused and action=='p':
        mixer.music.pause()
        is_paused=True

def manage_volume(action):
    if action=='-':
        mixer.music.set_volume(volume-0.9)
    if action=='+':
        mixer.music.set_volume(volume+0.9)

def close(action):
    if action=='e':
        mixer.music.stop()
        return True

def start():
    while True:
        action=input()
        if action=='c': choose_music()
        if close(action): break
        pause_music(action)
        manage_volume(action)

if '__main__'==__name__:
    start()
