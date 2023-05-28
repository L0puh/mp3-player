import pyglet
from pyglet.window import key

file = "music.mp3"

player = pyglet.media.Player()
music = pyglet.resource.media(file)
window = pyglet.window.Window()
label = pyglet.text.Label(file, x=window.width//2, y=window.height//2,
        anchor_x='center', anchor_y='center')

@window.event
def on_draw():
    window.clear()
    label.draw()

@window.event
def on_key_press(symbol, modifiers):
    player.queue(music)
    if symbol == key.SPACE:
        if player.playing:
            player.pause()
        else:
            player.play()

if '__main__' == __name__:
    pyglet.app.run()
