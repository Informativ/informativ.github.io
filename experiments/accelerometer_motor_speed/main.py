tilt = 0
while true:
    tilt = accelerometer.get_y()
    if tilt is >1023:
        pin0.write_analog(1023)
    elif tilt is <-1023:
        pin0.write_analog(-1023)
    else:
        pin0.write_analog(tilt)
