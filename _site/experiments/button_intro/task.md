# Introduksjon til knapper

I denne oppgaven skal vi se på hvordan man kan bruke knapper til å interagere med kode!


## Hva trenger du?

For å fullføre denne oppgaven trenger du:

* 2 knapper
* 4 han til hun kabler

![Oppsett](/assets/images/experiment_1.png?raw=true)

## Hvordan

For å fullføre denne oppgaven trenger vi kun å bruke en uendelig løkke (`while True`) og if tester (`if tingen-du-vil-sjekke`), slik:


{% highlight python %}
from microbit import microbit

while True:
	if test:
		det-som-skjer-hvis-test-er-sant
{% endhighlight %}

Så for eksempel (men ikke svar på oppgaven) vil denne koden sjekke om knapp A er trykket og så vise "Knapp A er trykket!".

{% highlight python %}
from microbit import microbit

while True:
	if button_a.is_pressed(): # test
		display.scroll("Knapp A er trykket!") # det-som-skjer-hvis-test-er-sant
{% endhighlight %}


I tillegg til dette må vi finne ut om en av knappene våre er trykket på!
Da må vi bruke `button_a.is_pressed()` og `button_b.is_pressed()` sammen med `if`-testen.

Men hvordan kan vi få bekreftelse på om dette faktisk har skjedd?
Jo da har microbiten en måte å vise "bilder" på! Bruk `display.show(...)` og et av bildene du [finner i listen her](http://microbit-micropython.readthedocs.io/en/latest/tutorials/images.html).
Så for eksempel:
{% highlight python %}
display.show(Image.HAPPY)
{% endhighlight %}

Til slutt, i enden av løkka, kan vi gjøre slik at disse bildene bare vises når knappene faktisk holdes nede.
Simpelthen legg til `display.clear()` helt i bunnen av løkken, på nivå med if-testen, slik:

``` python

import microbit

while True:
	if test:
		det-som-skjer-hvis-test-er-sant
		sleep(2000) # gjoer at den ikke clearer bildet med en gang
	display.clear()

```

Lykke til!
