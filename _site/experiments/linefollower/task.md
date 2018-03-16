# Linjefølger!

## Hva trengs? 
* Linjefølgerrobot
* micro:bit kortet


## Hvordan
Du trenger to kommandoer for å styre motorene:
* `pin12.write_digital(1)` (venstre motor)
* `pin16.write_digital(1)` (høyre motor)  

<br><br>

Deretter trenger du tre kommandoer for å lese informasjon fra sensorene. Disse gir enten tallet 0 eller 1 tilbake. 0 når den er over teipen, 1 når den er over den blanke overflaten.
* `pin13.read_digital()` (høyre sensor)
* `pin14.read_digital()` (midtre sensor)
* `pin15.read_digital()` (venstre sensor)  

<br><br>

For å sjekke om en sensor er aktiv kan du for eksempel skrive
``` python
if pin13.read_digital() is 0:
  "kode du vil gjøre om høyre sensor er over teipen"
```

