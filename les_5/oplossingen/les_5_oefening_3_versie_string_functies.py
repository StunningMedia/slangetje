#  hier een paar strings die we als invoer gaan gebruiken
adres = "François Backeljau, gamma-straat 12, 1234 Niethier"
adres2 = "Pieter-Jan Van Someren, Begijnhofweg 33a, 2600 Berchem"
adres3 = "Theo Dollars, Overlo 29, 9800 Deinze"
adres4 = "Emma Zwaluw, Shuttlelaan 283, 1000 Brussel"
spatie = " "
komma = ","
nieuwe_lijn = "\n"

# we maken een functie om een string te splitsen op de eerste spatie
# die kunnen we gaan gebruiken om voornaam en achternaam uit elkaar te trekken
#  en ook om straat en huisnummer uit elkaar te trekken
def splits_op_eerste_spatie(string_met_mogelijks_meerdere_spaties):
    positie_eerste_spatie = string_met_mogelijks_meerdere_spaties.find(" ")
    eerste_deel = string_met_mogelijks_meerdere_spaties[:positie_eerste_spatie]
    tweede_deel = string_met_mogelijks_meerdere_spaties[positie_eerste_spatie + 1:]
    
    return eerste_deel, tweede_deel

# we maken een functie 'splits_op' die een gegeven string uit elkaar trekt 
def splits_op(adres_string):
  # we splitsen de lijst eerst op in de 3 delen (via de komma)
  naam_deel, straat_deel, gemeente_deel = adres_string.split(komma)

  # dan splitsen we elk deel van de lijst op via de spatie naar de juiste variabelen
  voornaam, familienaam = splits_op_eerste_spatie(naam_deel.strip())
  straat, huisnummer = splits_op_eerste_spatie(straat_deel.strip())
  postnummer, gemeente = gemeente_deel.strip().split(spatie)
 
  return voornaam, familienaam, straat, huisnummer, postnummer, gemeente

# nu nog een mooie functie om alle gegevens af te drukken
def druk_gegevens_af(voornaam, familienaam, straat, huisnummer, postnummer, gemeente):
  print("Voornaam:", voornaam)
  print("Familienaam", familienaam)
  print("Straat:", straat)
  print("Huisnummer:", huisnummer)
  print("Postnummer:", postnummer)
  print("Gemeente", gemeente)

# nu nog een functie om opgave en uitgesplitste gegevens af te drukken
def splits_adres_string_en_druk_af(adres_string):
    print(adres_string, "wordt")
    voornaam, familienaam, straat, huisnummer, postnummer, gemeente = splits_op(adres_string)
    druk_gegevens_af(voornaam, familienaam, straat, huisnummer, postnummer, gemeente)
    print(nieuwe_lijn)

# en tenslotte de aanroepen met de verschillende adressen
splits_adres_string_en_druk_af(adres)
splits_adres_string_en_druk_af(adres2)
splits_adres_string_en_druk_af(adres3)
splits_adres_string_en_druk_af(adres4)
