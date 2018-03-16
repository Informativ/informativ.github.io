# USB

I denne oppgaven skal vi se på hvordan man kan sende informasjon mellom en Micro:bit og en PC over USB

## Hva trenger du?

For å fullføre denne oppgaven trenger du:

Ingenting!

## Hvordan

I microbit finnes det en UART modul som kan brukes til å sende data over USB.
For å bruke denne må vi initialisere uart med `uart.init()`.
Etter dette kan vi begynne å sende data med `uart.write()`. Denne funksjonen tar inn en byte variabel, så vi må gjøre om meldingen vår til bytes.

{% highlight python %}

melding = "Hei fra Micro:bit"

uart.write(bytes(melding, 'utf-8'))

{% endhighlight %}

Nå må vi lage et program for å ta i mot meldingen på PC. 

Vi kan bruke python med pyserial for å lese fra USB. Importer denne med `import serial`.
Pyserial kan brukes til å lese/skrive fra flere ting, så den må få beskjed om hvor den skal lese fra. 

I Windows leser vi fra USB med å hente informasjon i 'COM0', 'COM1', osv. I 'Enhetsbehandling' finner du hvilken COM Micro:bit er koblet til.

I Linux leser vi fra '/dev/ttyACM0', eller '/dev/ttyUSB0'. Hvilken din PC bruker finner du med å skrive 'ls /dev/' i terminalen.

{% highlight python %}

ser = serial.Serial('/dev/ttyACM0', 9600)

try:
    #Les fra USB
except:
    pass    
{% endhighlight %}

Etter du har valgt hvor du leser fra kan vi begynne å lese. Dette må gjøres i en try / except blokk, fordi det ikke er sikkert at den klarer å lese noe data. 
Pyserial leser bytes fra USB med `ser.read()` eller `ser.readline()`.
