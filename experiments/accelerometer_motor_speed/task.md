# Akselerometer styrt motor

I denne oppgaven skal vi bruke samme oppsett som i motor-oppgaven,
men i stedet for at den skal gå konstant så skal vi bruke **akselerometeret**
på microbiten til å styre motoren.

Med et akselerometer kan vi finne ut hvor fort en gjenstand går i en bestemt retning,
eller hvor mye tilt en gjenstand har.

## Hva trengs?
* 1 Transistor
* 1 2.2k Ohm resistor
* 1 Terminal Tilkobling
* 1 Motor
* 3 Han til hun kabel
* 1 Vifteblad

## Hvordan
For å løse denne oppgaven må vi som sagt i introduksjonen bruke **akselerometeret** til microbiten.
Dette kan vi gjøre med `accelerometer` modulen.
For å få hvor mye tilt microbiten har for øyeblikket må vi enten bruke `accelerometer.get_x()` eller `accelerometer.get_y()`.
Disse vil gi en verdi for `x` eller `y` aksen respektivt.

Nå som vi har en tilt-verdi må vi bruke denne for å kjøre motoren.
Da er det vel bare å bruke `write_analog(verdi)` for å drive motoren, ikke sant?
Det er det dessverre ikke, for pinnene på microbiten går kun fra -1023 til 1023 så vi må ta hensyn til dette når vi skriver koden vår.
Vi kan løse dette ved å sjekke om verdien er over eller under +-1023, og deretter sette inn -1023 eller 1023.
Ellers er det bare å skrive tilt-verdien rett til motoren.
