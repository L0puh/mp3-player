import os, pygame
from pygame import mixer
from config import directory
from main import close
import actions

songs=[]

def playlist():
    [songs.append(song) for song in os.listdir(directory)]
    mixer.music.load(os.path.join(directory, songs.pop()))
    mixer.music.queue(os.path.join(directory, songs.pop()))
    mixer.music.set_endevent(pygame.USEREVENT)
    mixer.music.play()
    next_song()

def next_song():
    while True:
        for event in pygame.event.get():
            close(event)
            if event.type == pygame.KEYDOWN:
                actions.get_action(event)
            if event.type == pygame.USEREVENT:
                if len (songs) > 0:
                    mixer.music.queue(os.path.join(directory, songs.pop()))
                else: return
