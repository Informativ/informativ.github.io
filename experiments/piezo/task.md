# Høyttaler

I denne oppgaven skal vi ekspandere [knappe-oppgaven](https://informativ.github.io/microbit-oppgaver/experiments/button_intro/task).
Forskjellen her er at vi skal få en høyttaler til å spille av lyd når vi trykker på knappene.

## Hva trenger vi?
* 1 Piezo Element
* 2 Han til hun kabel

## Hvordan
Først må musikk importeres. Skriv `import music` på linja under `from microbit import *`.

Bruk så knappe-oppgaven som base og fjern alt som har med `display` å gjøre, og bytt dette ut med `music.pitch(frekvens, tid-i-ms)`.

<br><br>
Du kan nå spille toner med knappene!

Eksempelvis kan du bruke frekvensene `440` og `880` for å spille to A-er som er en oktav mellom hverandre.
Hvis du vil se flere frekvenser kan du sjekke ut [denne nettsiden](http://www.phy.mtu.edu/~suits/notefreqs.html).

Prøv å legge til flere knapper slik at du kan lage et mini-piano!
