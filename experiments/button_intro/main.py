# Add your Python code here. E.g.
from microbit import *


while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        display.show(Image.SAD)
    display.clear()