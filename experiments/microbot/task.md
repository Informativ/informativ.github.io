# Microbot
I denne oppgaven skal vi lage en søt liten robot som blir sur hvis den detter på ryggen.

##Hva trenger vi?
* Microbot 3D-printet kasse. (Spør en foredragsholder hvis du ikke har)

## Hvordan

Det første vi trenger er å lage cutom bilder på LED-matrisen. Da bruker vi `image = Image("00000:00000:00000:00000:00000:")`. Tallene går fra 0 til 9 og indikerer hvor sterkt en LED lyser. Hver serie med tall er en rad i matrisen (går fra topp til bunn). Prøv å få roboten til å smile! 

Nå som vi har fått roboten til å smile må vi gi den noen humørsvingninger! I dette tilfellet trenger vi tiltverdien til `y` aksen, for å se om roboten står eller ligger på ryggen. Husker du ikke hvordan kan du gå til oppgave 7. 
