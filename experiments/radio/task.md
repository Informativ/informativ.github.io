# Radio

I denne oppgaven skal vi se på hvordan man kan bruke Micro:bit sin radio til å sende meldinger mellom flere Micro:bit

## Hva trenger du?

For å fullføre denne oppgaven trenger du:

* 2 eller flere Micro:bit

## Hvordan
**Før vi begynner må du legge til `import radio` rett under `from microbit import *`.**

Radio med Micro:bit virker på samme måte som en Walkietalkie. 
Dette betyr at alle som er koblet på samme kanal kan sende beskjeder, og mota beskjeder. Dette er veldig fint hvis man vil at mange Micro:bit skal få den samme beskjeden.
Det negative ved dette er at det kan bli veldig kaotisk og vi kan få inn beskjeder som ikke er ment for oss. 
Hvis du ikke vil få inn meldingene til alle andre i klassen din bør du derfor ikke velge standard kanalen for radio.

{% highlight python %}
from microbit import microbit
import radio

radio.config(channel=42)

{% endhighlight %}

Det finnes mange muligheter til å konfigurere radio. * [microbit micropython radio dokumentasjon](http://microbit-micropython.readthedocs.io/en/latest/radio.html)


Får å bruke radio må vi skru den på med `radio.on()`, og nå er vi klare for å sende meldinger. 
Vi kan bruke den ene Micro:bit til å sende en melding med `radio.send("Melding")`, og den andre til å mota en melding med `radio.receive()`.
Nå har vi motatt meldingen, men kan fortsatt ikke se den. For å vise meldingen bruker vi `display.show`.

Til slutt er det god kodeskikk å skru av radioen med `radio.off`.
