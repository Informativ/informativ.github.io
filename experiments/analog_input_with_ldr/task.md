# Lysmåler

I denne oppgaven skal vi bygge videre på det vi gjorde i [knappe-oppgaven](https://informativ.github.io/microbit-oppgaver/experiments/button_intro/task),
men i steden for å bruke knapper skal vi bruke lys for å bytte bildet på skjermen!

## Hva trenger du?

* 1 lyssensor
* 1 10k Ohm resistor
* 3 han til hun kabler

## Hvordan

Som i knappe-oppgaven trenger vi en uendelig løkke og `if`-tester,
men i denne oppgaven skal vi også bruke variabler!

Variabler blir i programmering brukt for å lagre data slik at man kan bruke det senere og gjøre kode lettere å lese.
Måten man *deklarerer* et variabel er ved å sette et navn lik et utrykk, for eksempel `navn = "Bob"`.

I denne oppgaven bruker vi da `pin 0` på microbiten til å hente data fra lys-sensoren vår.
For å bruke denne dataen lager vi et variabel `lysstyrke` og setter det lik `pin0.read_analog()`.
Det dette gjør er å sette `lysstyrke` til den analoge verdien av pin 0.

Nå kan vi bruke denne verdien til å sjekke om det kommer lys inn i sensoren!
Sjekk om lysstyrke er større enn 512, og vis så et bilde med `display.show(...)`, ellers (med `else`) vis et annet bilde.

`pin0.read_analog()` vil gi en verdi fra 0 til 1024, så prøv å forandre på verdien og sjekk hvordan dette endrer sensitiviteten på lyssensoren!