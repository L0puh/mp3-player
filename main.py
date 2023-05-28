from pygame import mixer

mixer.init()
file = 'music.mp3'

mixer.music.load(file)
mixer.music.play()
is_paused = False
volume = mixer.music.get_volume()

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
        if close(action): break
        pause_music(action)
        manage_volume(action)

if '__main__'==__name__:
    start()
