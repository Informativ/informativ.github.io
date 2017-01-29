# Introduksjon til knapper

I denne oppgaven skal vi se på hvordan man kan bruke knapper til å interagere med kode!

## Hva trenger du?

For å fullføre denne oppgaven trenger du:

* 2 knapper
* 4 han til hun kabler

## Hvordan

For å fullføre denne oppgaven trenger vi kun å bruke en uendelig løkke (`while True`) og if tester (`if tingen-du-vil-sjekke`).
I tillegg til dette må vi finne ut om en av knappene våre er trykket på!
Da må vi bruke `button_a.is_pressed()` og `button_a.is_pressed()` sammen med en `if`-test.

Men hvordan kan vi få bekreftelse på om dette faktisk har skjedd?
Jo da har microbiten en måte å vise "bilder" på! Bruk `display.show(...)` og et av bildene du [finner i listen her](http://microbit-micropython.readthedocs.io/en/latest/tutorials/images.html).

Til slutt, i enden av løkka, kan vi gjøre slik at disse bildene bare vises når knappene faktisk holdes nede.
Simpelten legg til `display.clear()` helt i bunnen av løkka, og så skal bildet forsvinne i det knappen slippes.

Lykke til!
