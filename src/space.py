from ursina import *

def update():
    global offset

    offset += time.dt*.3
    setattr(bg, "texture_offset", (offset, 0))

app = Ursina()

offset = 0
bg=Entity(model="quad", scale=(20, 10), texture="assets/bg.jpeg", z=.1)
bird = Animation("assets//bird", scale=(1.3, .8), y=1.5)

app.run()
