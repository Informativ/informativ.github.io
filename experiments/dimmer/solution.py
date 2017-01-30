from microbit import *

lys_aktivt = False

while True:
    if pin0.is_touched():
        if lys_aktivt:
            lys_aktivt = False
        else:
            lys_aktivt = True
    
    if lys_aktivt:
        lys_styrke = pin1.read_analog()
        pin2.write_analog(lys_styrke)
    else:
        pin2.write_digital(0)
