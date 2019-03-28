# Viftemotor

I denne oppgaven skal vi bruke en motor for å kjøre en vifte.

## Hva trengs?
* 1 Transistor
* 1 2.2k Ohm resistor
* 1 Terminal Tilkobling
* 1 Motor
* 3 Han til hun kabel
* 1 Vifteblad

![Oppsett](/assets/images/experiment_4.png?raw=true)

## Hvordan
Siden vi skal ha en konstant kjørende motor i denne oppgaven trenger vi kun en variabel som kan ta vare på tilstanden til motoren og et par løkker.

Først må vi lage en variabel som holder på den nåværende tilstanden til motoren. Plasser denne over den uendelige løkka og sett den til å være `0`.
Hadde ikke variabelen vår vært utenfor løkken ville motorens hastighet blitt satt til null hver gang vi kjører gjennom (det ønsker vi ikke).

Videre skal vi lage to løkker slik at vi får vekslende signal.
Med dette mener vi at duty skal variere opp og ned mellom `0` og `1024`.
Inne i disse løkene skal vi *inkrementere* (`variabel += 1`) og *dekrementere* (`variabel -= 1`) tilstands-variablet vårt,
og deretter skrive til outputen vår ved hjelp av `pin0.write_analog(variabel)`.

Du skal nå ha en fin liten vifte!

Se om du greier å få vifta til å gå saktere! Tips: `sleep(...)`
