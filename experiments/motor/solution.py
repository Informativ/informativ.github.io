from microbit import *

duty = 0

while True:
    while duty < 1023:
        duty += 1
        pin0.write_analog(duty)
    while duty > 0:
        duty -= 1
        pin0.write_analog(duty)
