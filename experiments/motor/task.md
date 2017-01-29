# Viftemotor

I denne oppgave skal vi bruke en motor for å kjøre en vifte.

## Hva trengs?
TODO

## Hvordan
Siden vi bare skal ha en konstant kjørende motor i denne oppgaven trenger vi bare et variabel som holder på tilstanden til motoren og noen løkker.

Først må vi lage et variabel som holder på den nåværende tilstanden til motoren. Plasser denne utenfor den uendelige løkka og deklarer den til å være `0`.
Hadde vi ikke plassert den utenfor løkka ville vi endt opp med at motoren sto stille hele tiden!

Videre skal vi lage to løkker slik at vi får vekslende signal.
Med dette mener vi at duty skal variere opp og ned mellom `0` og `1024`.
Inne i disse løkene skal vi **inkrementere** (`variabel += 1`) og **dekrementere** (`variabel -= 1`) tilstands-variablet vårt,
og deretter skrive til outputen vår ved hjelp av `pin0.write_analog(variabel-navn)`.

Du skal nå ha en fin liten vifte!

Se om du greier å få vifta til å gå saktere! Tips: `sleep(...)`
