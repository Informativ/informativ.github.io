# Python Basics & Hjelpemiddler
På denne siden kan du finne diverse informasjon som kan hjelpe deg når du skriver oppgavene!

## Syntax
* While-løkke:
{% highlight python %}
    while test:
        kode-som-kjøres-så-lenge-"test"-er-sann
{% endhighlight %}
* Array med tekst:
{% highlight python %}
    mangeOrd = ["Hei", "kanskje", "ja", "nei", "vet ikke"]
{% endhighlight %}
* If-setning:
{% highlight python%}
    if test:
        det-som-skal-skje-hvis-"test"-er-sann
    else:
        det-som-skal-skje-hvis-"test"-er-usann
{% endhighlight %}

### Indentering
I motsetning til mange andre språk så bruker python **indentering** for å holde styr på **blokker**.
Dette betyr at indentering er ekstremt viktig når du skriver python kode.

Eksempel:
{% highlight python %}
    if test1:
        uttrykk1
        uttrykk2

    if test2:
        uttrykk3
    uttrykk4
{% endhighlight %}

I dette eksempelet vil uttrykk 1 og 2 bare kjøre hvis test1 er sann.
uttrykk 3 vil derimot bare kjøre hvis test2 er sann, men uttrykk4 vil alltid kjøre! Vi kan altså se at uttrykk1 og uttrykk2 "tilhører" test1 fordi de er satt hakket innenfor test1. Uttrykk3 hører til test2, mens uttrykk4 ikke gjør det, siden den ikke er et hakk innenfor test2.

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
* `random.choice(arrayobjekt)` - Denne funksjonen gir oss et tilfeldig objekt fra en array. `arrayobjekt` kan for eksempel byttes ut med `mangeOrd` som er fra **Syntax**.
* `display.show("min melding")` - Viser en scrollende tekst på LED'ene til micro:bit'en.
* `displar.clear()` - Fjerner eventuelle bilder som er på micro:bit'en.
* `sleep(millisekunder)` - Koden venter i angitte millisekunder før den fortsetter å kjøre. 
