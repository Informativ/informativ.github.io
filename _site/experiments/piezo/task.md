# Høyttaler

I denne oppgaven skal vi ekspandere [knappe-oppgaven](https://informativ.github.io/microbit-oppgaver/experiments/button_intro/task).
Forskjellen her er at vi skal få en høyttaler til å spille av lyd når vi trykker på knappene.

## Hva trenger vi?
* 1 Piezo Element
* 2 Han til hun kabel

![Oppsett](/assets/images/experiment_6.png?raw=true)

## Hvordan
Vi skal nå få et Piezo element til å spille av musikk.<br>
Her har du et eksempel på et program som spiller av en frekvens `440` i 2 sekunder.
{% highlight python %}
from microbit import microbit
import music
while True:
	music.pitch(440, 2000)
	sleep(1000)
{% endhighlight %}
Under er det forklart hvordan du skal gå frem for denne oppgaven.

Først må musikk importeres. <br>
Skriv `import music` på linja under `from microbit import *`.

Bruk så knappe-oppgaven som base og fjern alt som har med `display` å gjøre, og bytt dette ut med `music.pitch(frekvens, tid-i-ms)`.
<br><br>
Du kan nå spille toner med knappene!

Eksempelvis kan du bruke frekvensene `440` og `880` for å spille to A-er som er en oktav mellom hverandre.
Hvis du vil se flere frekvenser kan du sjekke ut [denne nettsiden](http://www.phy.mtu.edu/~suits/notefreqs.html).


