from microbit import *

while True:
    lysstyrke = pin0.read_analog()
    
    if lysstyrke > 512:
        display.show(Image.YES)
    else:
        display.show(Image.NO)
