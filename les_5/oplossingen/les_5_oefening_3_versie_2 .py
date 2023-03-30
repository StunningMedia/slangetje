import os

#  dit is de string die we als invoer gaan gebruiken
adres = "François Backeljau, gamma-straat 12, 1234 Niethier"
spatie = " "
komma = ","

# we maken eerst een functie 'splits_op' die een lijn uit elkaar trekt in voornaam, naam en adres
def splits_op(adres_string):
  # De voornaam is alles voor de eerste spatie
  positie1 = adres_string.find(" ")
  voornaam = adres_string[:positie1]
  
  # De familienaam is alles na de spatie en voor de komma
  positie2 = adres_string.find(",")
  familienaam = adres_string[positie1 + 1:positie2]
  
  # Het adres is dan al de rest
  adres = adres_string[positie2 + 2:]
  
  # De straat is alles voor de spatie
  positie1 = adres.find(spatie)
  straat = adres[:positie1]
  
  # Het huisnummer is alles na de spatie & voor de komma
  positie2 = adres.find(komma)
  huisnummer = adres[positie1 + 1:positie2]

  #de plaats is dan al de rest
  plaats = adres[positie2 + 2:]
  
  # Belgische postnummers zijn altijd 4 cijfers
  postnummer = plaats[0:4]
  
  # Omdat postnummers altijd 4 cijfers zijn, begint de gemeente altijd op 5
  gemeente = plaats[5:]

  # resultaten teruggeven
  return voornaam, familienaam, straat, huisnummer, postnummer, gemeente

# hier de print-functie
def druk_gegevens_af(voornaam, familienaam, straat, huisnummer, postnummer, gemeente):
  print("Voornaam:", voornaam)
  print("Familienaam", familienaam)
  print("Straat:", straat)
  print("Huisnummer:", huisnummer)
  print("Postnummer:", postnummer)
  print("Gemeente:", gemeente)
  print('\n')
  print('\n')

# functie aanroepen om op te spliten
voornaam, familienaam, straat, huisnummer, postnummer, gemeente = splits_op(adres)
# functie aanroepen om af te drukken
druk_gegevens_af(voornaam, familienaam, straat, huisnummer, postnummer, gemeente)

# hieronder definiëren we nog drie extra adressen.  Zorg er met code voor dat deze ook alle drie netjes worden afgedrukt.  Je zal daarvoor elk adres moeten uit elkaar trekken en daarna afdrukken
adres2 = "Pieter-Jan Van Someren, Begijnhofweg 33a, 2600 Berchem"
adres3 = "Theo Dollars, Overlo 29, 9800 Deinze"
adres4 = "Emma Zwaluw, Shuttlelaan 283, 1000 Brussel"


voornaam, familienaam, straat, huisnummer, postnummer, gemeente = splits_op(adres2)
druk_gegevens_af(voornaam, familienaam, straat, huisnummer, postnummer, gemeente)

voornaam, familienaam, straat, huisnummer, postnummer, gemeente = splits_op(adres3)
druk_gegevens_af(voornaam, familienaam, straat, huisnummer, postnummer, gemeente)

voornaam, familienaam, straat, huisnummer, postnummer, gemeente = splits_op(adres4)
druk_gegevens_af(voornaam, familienaam, straat, huisnummer, postnummer, gemeente)
