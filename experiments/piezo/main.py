from microbit import *

while True:
    if button_a.is_pressed():
        music.pitch(440, 500)
    elif button_b.is_pressed():
        music.pitch(700, 500)

