# Python Basics & Hjelpemiddler
På denne siden kan du finne diverse informasjon som kan hjelpe deg når du skriver oppgavene!

## Syntax
### Indentering
I motsetning til mange andre språk så bruker python **indentering** for å holde styr på **blokker**.
Dette betyr at indentering er ekstremt viktig når du skriver python kode.

Eksempel:
{% highlight python %}
    if test1:
        utrykk1
        utrykk2

    if test2:
        utrykk3
    utrykk4
{% endhighlight %}

I dette eksempelet vil utrykk 1 og 2 bare kjøre hvis test1 er sann.
Utrykk 3 vil derimot bare kjøre hvis test2 er sann, men utrykk4 vil alltid kjøre!

### Typer
Python er et såkalt dymaisk typet språk.
Dette betyr at vi ikke trenger å spesifisere hvilken type en variabel er.
For å definere en variabel trenger vi bare å skrive `navn = verdi`.
Det trengs ikke noe `int` eller lignende. Hvilken type verdien er finner python ut selv!

Vær obs på at hvis du vil ha et desimaltall tilbake når du deler, så må **divisoren** være et desimaltall.

## Nyttige funskjoner
Her er noen nyttige funksjoner som du kan få bruk for når du skriver python:

* `str(verdi)` - Denne funksjonen gjør en verdi om til en streng.
  Dette er spesielt nyttig hvis man har lyst til å skrive ut et tall.
* `len(objekt)` - Denne funksjonen gir lengden av et objekt.
  For eksemepel hvor mange bokstaver en streng inneholder, eller antall elementer i en array.
