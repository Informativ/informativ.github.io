from microbit import *

tilt = 0
happyFace = Image("00000:00000:99999:90009:09990")
sadFace = Image("00000:00000:09990:90009:99999")

while True:
    tilt = accelerometer.get_y()

    if tilt < -700:
        display.show(happyFace)
    elif tilt > -700:
        display.show(sadFace)

