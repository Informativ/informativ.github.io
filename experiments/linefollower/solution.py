import microbit import *

while True:
    if pin13.read_digital() is 0:
        pin12.write_digital(1)
        pin16.write_digital(0)
    if pin14.read_digital() is 0:
        pin12.write_digital(1)
        pin16.write_digital(1)
    if pin15.read_digital() is 0:
        pin12.write_digital(0)
        pin16.write_digital(1)
