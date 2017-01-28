tilt = 0
while true:
    #vi setter variabelen tilt lik verdien til accelerometer.get_y().
    #denne verdien forteller oss hvor mye micro:bit'en har blitt tiltet.
    tilt = accelerometer.get_y()

    #vi sender verdien til tilt til pin0, som sier hvor fort
    #motoren skal gå. Verdien må være mellom -1023 og 1023, så vi har
    #to if-setninger som håndterer dette. 
    if tilt > 1023:
        pin0.write_analog(1023)
    elif tilt < -1023:
        pin0.write_analog(-1023)
    else:
        pin0.write_analog(tilt)
