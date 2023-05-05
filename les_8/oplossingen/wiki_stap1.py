import wikipedia

# functie "vind_pagina_namen"
# neemt 1 parameter "Zoekterm", en geeft lijst van pagina's terug
def vind_pagina_namen(zoekterm):
    return wikipedia.search(zoekterm)

# functie "print_lege_regel"
# geen parameters, drukt 1 lege regel af
def print_lege_regel():
    print()

# functie "vraag_zoekterm"
#  geen parameters
# vraagt een zoekterm aan de gebruiker en geeft die terug als resultaat van de functie
def vraag_zoekterm():
    return input("Geef een zoekterm: ")

# functie "print_lijst_van_paginas"
# neemt 1 parameter "pagina_namen" en drukt de lijst van titels af
def print_lijst_van_paginas(pagina_namen):
  # vul variabele met het aantal pagina's in de lijst
    aantal_paginas = len(pagina_namen)

    print("Dit zijn de " + str(aantal_paginas) + " meest relevante pagina's hierover: ")
  # zet volgnummer op 1
    nummer = 1

  # voor elke pagina_naam in pagina_namen ...
    for pagina_naam in pagina_namen:
        #  druk een volgnummer en de pagina_naam af
        print(str(nummer) + ". " + pagina_naam)
        # verhoog volgnummer
        nummer = nummer + 1
      
  # druk tenslotte een lege regel af
    print_lege_regel()


# de hoofd-functie "wiki"
# geen parameters
def wiki():
    # taal op NL zetten
    wikipedia.set_lang("nl")
    # init zoekterm op eerste vraag aan gebruiker
    zoekterm = vraag_zoekterm()

    # zolang de zoekterm niet '<stop>' is ...
    while not zoekterm == "<stop>":        
        # druk lege regel af
        print_lege_regel()
        # zoek de pagina namen voor de zoekterm
        pagina_namen = vind_pagina_namen(zoekterm)
        # druk de gevonden pagina namen af
        print_lijst_van_paginas(pagina_namen)
        # vraag een nieuwe zoekterm
        zoekterm = vraag_zoekterm()



# aanroep van de hoofd-functie
wiki()