import os, pygame
from pygame import mixer
songs=[]

def playlist(folder):
    [songs.append(song) for song in os.listdir(folder)]
    mixer.music.load(os.path.join(folder, songs.pop()))
    mixer.music.queue(os.path.join(folder, songs.pop()))
    mixer.music.set_endevent(pygame.USEREVENT)
    mixer.music.play()
    next_song(folder)

def next_song(folder):
    from main import get_action, close

    while True:
        for event in pygame.event.get():
            close(event)
            if event.type == pygame.KEYDOWN:
                get_action(event.key)
            if event.type == pygame.USEREVENT:
                if len (songs) > 0:
                    mixer.music.queue(os.path.join(folder, songs.pop()))
                else: return
