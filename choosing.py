from pygame import mixer
import os
from interface import print_text
from config import directory, black

def choose_music():
    songs=[i for i in os.listdir(directory)]
    count =0
    for n, song in enumerate(songs):
        count += 30
        print_text(f'{n+1}: {song}', (0, count))
    return songs

def play_music(song):
    mixer.music.load(song)
    mixer.music.queue(song)
    mixer.music.play()
    print_text(f'{song} is playing', (0,0), black)
    return

def define_choice(songs, event):
    try:
        choice = int(event.unicode)-1
        play_music(os.path.join(directory, songs[choice]))
    except:
        print_text('opss', (0,0), black)

