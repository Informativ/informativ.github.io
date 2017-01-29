# Lysm�ler

I denne oppgaven skal vi bygge videre p� det vi gjorde i [knappe-oppgaven](https://informativ.github.io/microbit-oppgaver/experiments/button_intro/task),
men i steden for � bruke knapper skal vi bruke lys for � bytte bildet p� skjermen!

## Hva trenger du?

* 1 lyssensor
* 1 10k Ohm resistor
* 3 han til hun kabler

## Hvordan

Som i knappe-oppgaven trenger vi en uendelig l�kke og `if`-tester,
men i denne oppgaven skal vi ogs� bruke variabler!

Variabler blir i programmering brukt for � lagre data slik at man kan bruke det senere og gj�re kode lettere � lese.
M�ten man *deklarerer* et variabel er ved � sette et navn lik et utrykk, for eksempel `navn = "Bob"`.

I denne oppgaven bruker vi da `pin 0` p� microbiten til � hente data fra lys-sensoren v�r.
For � bruke denne dataen lager vi et variabel `lysstyrke` og setter det lik `pin0.read_analog()`.
Det dette gj�r er � sette `lysstyrke` til den analoge verdien av pin 0.

N� kan vi bruke denne verdien til � sjekke om det kommer lys inn i sensoren!
Sjekk om lysstyrke er st�rre enn 512, og vis s� et bilde med `display.show(...)`, ellers (med `else`) vis et annet bilde.

`pin0.read_analog()` vil gi en verdi fra 0 til 1024, s� pr�v � forandre p� verdien og sjekk hvordan dette endrer sensitiviteten p� lyssensoren!