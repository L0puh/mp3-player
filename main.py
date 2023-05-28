from pygame import mixer

mixer.init()
file = 'music.mp3'

mixer.music.load(file)
mixer.music.play()
is_paused = True

def pause_music():
    global is_paused
    if is_paused:
        mixer.music.unpause()
        is_paused = False
    else:
        mixer.music.pause()
        is_paused=True

def start():
    while True:
        action=input()
        if action=='p':
            pause_music()
        if action=='e':
            mixer.music.stop()
            break

if '__main__'==__name__:
    start()
