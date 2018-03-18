# Dimmer

I denne oppgaven skal vi lage en dimmer, akkurat slik som man har i veggen hjemme (dog litt mindre skala).

## Hva trengs?
* 1 Dimmer
* 1 x Ohm resistor
* 1 LED
* 1 Knapp
* 7 Han til hun kabler

![Oppsett](/assets/images/experiment_3.png?raw=true)

## Hvordan
For å løse denne oppgaven trenger vi noen `if`-er inne i en uendelig løkke.
Disse `if`-ene skal sjekke to ting:

*Er lyset slått på?* \\
Hvis lyset er slått på må vi sjekke den nåværende statusen til dimmeren.
For å gjøre dette må vi bruke `read_analog()` på pinen som dimmeren er koblet på.
Deretter må vi putte denne verdien på pinnen som LED-en vår er koblet på.
Dette gjøres ved å bruke `write_analog(verdi)` på pinen som blir brukt.

Hvis lyset derimot ikke er slått på, trenger vi simpelten bare å gi den et null signal.

*Har noen trykket på av/på knappen?* \\
I så fall må vi skifte den nåværende statusen på lyset til det omvendte av det den er nå.
**Tips:** Bruk `not` for å få det omvendte av den nåværende veriden.

## Ekstraoppgave
Prøv å koble til flere LEDs!
