#  dit is de string die we als invoer gaan gebruiken
adres = "François Backeljau, gamma-straat 12, 1234 Niethier"

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

  # de drie variabelen teruggeven als resultaat
  return voornaam, familienaam, adres

# we maken een functie "druk_gegevens_af" die drie parameters binnenkrijgt  (voornaam, familienaam en adres) en die netjes gelabeld afdrukt
def druk_gegevens_af(voornaam, familienaam, adres):
  print("Voornaam:", voornaam)
  print("Familienaam", familienaam)
  print("Adres:", adres)

# hier roepen we de functie 'splits_op' aan om drie variabelen mee te vullen
voornaam, familienaam, adres = splits_op(adres)
# en tenslotte roepen we functie "druk_gegevens_af" aan op de uitgesplitste gegevens te tonen
druk_gegevens_af(voornaam, familienaam, adres)

# hieronder definiëren we nog drie extra adressen.  Zorg er met code voor dat deze ook alle drie netjes worden afgedrukt.  Je zal daarvoor elk adres moeten uit elkaar trekken en daarna afdrukken
adres2 = "Pieter-Jan Van Someren, Begijnhofweg 33a, 2600 Berchem"
adres3 = "Theo Dollars, Overlo 29, 9800 Deinze"
adres4 = "Emma Zwaluw, Shuttlelaan 283, 1000 Brussel"


voornaam, familienaam, adres = splits_op(adres2)
druk_gegevens_af(voornaam, familienaam, adres)

voornaam, familienaam, adres = splits_op(adres3)
druk_gegevens_af(voornaam, familienaam, adres)

voornaam, familienaam, adres = splits_op(adres24)
druk_gegevens_af(voornaam, familienaam, adres)