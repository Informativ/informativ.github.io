# 8-ball
I denne oppgaven skal vi lage en 8-ball. Når vi rister på micro:bit'en vil den gi oss et svar tilbake!

## Hva trenger vi?
* Ingenting!

## Hvordan
For å lage en 8-ball trenger vi to ting. Vi trenger å vite når kontrolleren blir ristet, og vi må kunne gi et tilfeldig svar.

La oss starte med risting. Micro:bit har mange "states", og en av disse heter "shake". For å sjekke om micro:bit'en har blitt ristet kan vi bruke `accelerometer.was_gesture("shake")` inni en if-setning.

Da har vi en sjekk for ristingen, så nå trenger vi svarene våre som skal vises hvis den har blitt ristet. Dette kan gjøres på mange måter, men vi skal her bruke `random.choice(arrayobjekt)`. Først må vi lage array'en vår (se [Python-hjelp](informativ.github.io/python_hjelp)), og så kan vi bruke `random.choice(arrayobjekt)` sammen med denne.

### Tips
Du kommer til å trenge `display.show(tekststreng)`, `display.clear()` og `sleep(millisekunder)`. Se [Python-hjelp](informativ.github.io/python_hjelp)
