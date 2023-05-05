import wikipedia
import warnings
warnings.simplefilter("ignore")

# functie "vind_pagina_namen":  idem stap 2
def vind_pagina_namen(zoekterm):
    return wikipedia.search(zoekterm)

# functie "zoek_suggestie":  idem stap 2
def zoek_suggestie(zoekterm):
    return wikipedia.suggest(zoekterm)

# functie "print_lege_regel":  idem stap 2
def print_lege_regel():
    print()

# functie "vraag_zoekterm":  idem stap 2
def vraag_zoekterm():
    return input("Geef een zoekterm: ")

# functie "print_lijst_van_paginas":  idem stap 2
def print_lijst_van_paginas(pagina_namen, aantal_paginas, zoekterm):
    if aantal_paginas == 0:
        print("Niks gevonden voor", zoekterm)
    else:
        print("Dit zijn de", str(aantal_paginas), "meest relevante pagina's over", zoekterm + ":")
        nummer = 1
        for pagina_naam in pagina_namen:
            print(str(nummer) + ". " + pagina_naam)
            vind_en_print_samenvatting(pagina_naam)
            nummer = nummer + 1

    print_lege_regel()

# functie "vind_en_print_samenvatting"
# bijna identiek aan stap 2, enkel nu met exception handling voor verwijspaginas
def vind_en_print_samenvatting(pagina_naam):
  # probeer ....
    try:
        # zoek de uitleg voor de pagina_naam, 1 zin lang
        uitleg = wikipedia.summary(pagina_naam, sentences=1)
        print(uitleg)
        print_lege_regel()
      # alleen let op, als het een verwijspagina bleek te zijn  ( er komt een disambiguationError op de proppen) druk dan een tekst af dat dit een verwijspagina is
    except wikipedia.exceptions.DisambiguationError as e:
        print("Deze pagina is een verwijspagina.")


# functie "vind_en_print_suggestie":  idem stap 2
def vind_en_print_suggestie(zoekterm):
    suggestie = zoek_suggestie(zoekterm)
    if suggestie != None:
        print("Niks gevonden voor", zoekterm)
        print_lege_regel()
        print("Maar misschien bedoelde je", suggestie + "?")
        pagina_namen = vind_pagina_namen(suggestie)
        print_lijst_van_paginas(pagina_namen, len(pagina_namen), zoekterm)


# functie "wiki":  idem stap 2
def wiki():
    wikipedia.set_lang("nl")
    zoekterm = vraag_zoekterm()
    print_lege_regel()

    while not zoekterm == "<stop>":
        pagina_namen = vind_pagina_namen(zoekterm)
        aantal_paginas = len(pagina_namen)

        if aantal_paginas == 0:
            vind_en_print_suggestie(zoekterm)
        else: 
            print_lijst_van_paginas(pagina_namen, aantal_paginas, zoekterm)

        zoekterm = vraag_zoekterm()

wiki()