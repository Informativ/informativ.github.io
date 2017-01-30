from microbit import *

while True:
    #vi leser av lysstyrken til LDR'en
    #koblet til pin0.
    lysstyrke = pin0.read_analog()
    
    if lysstyrke > 512:
        display.show(Image.YES)
    else:
        display.show(Image.NO)
