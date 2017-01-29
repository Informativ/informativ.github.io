# Lysmåler

I denne oppgaven skal vi bygge videre på det vi gjorde i [knappe-oppgaven](https://informativ.github.io/microbit-oppgaver/experiments/button_intro/task),
men i stedet for å bruke knapper skal vi bruke lys for å bytte bildet på skjermen!

## Hva trenger du?

* 1 lyssensor
* 1 10k Ohm resistor
* 3 han til hun kabler

## Hvordan

Som i knappe-oppgaven trenger vi en uendelig løkke og `if`-tester,
men i denne oppgaven skal vi også bruke variabler!

Variabler blir i programmering brukt for å lagre data slik at man kan bruke det senere og gjøre kode lettere å lese.
Måten man *deklarerer* en variabel på er ved å sette et navn lik et uttrykk, for eksempel `navn = "Bob"`.

I denne oppgaven bruker vi da `pin 0` på microbiten til å hente data fra lys-sensoren vår.
For å bruke denne dataen lager vi et variabel `lysstyrke` og setter det lik `pin0.read_analog()`.
```python
variabelnavn = pin0.read_analog()
``` 
Det dette gjør er å sette `lysstyrke` til den analoge verdien av pin 0. Den analoge verdien er et mål på hvor mye lys den registrerer.

Nå kan vi bruke denne verdien til å sjekke om det kommer lys inn i sensoren!
Sjekk om lysstyrke er større enn 512, og er den det så vis et bilde med `display.show(...)`, hvis ikke (med `else`) vis et annet bilde. 
```python
if testen-din:
  kode-som-skal-skje
else:
  kode-som-skal-skje
```


`pin0.read_analog()` vil gi en verdi fra 0 til 1024, så prøv å forandre på verdien i if-setningen og se hva det gjør!
