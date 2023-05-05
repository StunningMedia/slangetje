import wikipedia

# functie "vind_pagina_namen":  idem stap 1
def vind_pagina_namen(zoekterm):
    return wikipedia.search(zoekterm)

# functie "print_lege_regel":  idem stap 1
def print_lege_regel():
    print()

# functie "vraag_zoekterm":  idem stap 1
def vraag_zoekterm():
    return input("Geef een zoekterm: ")

# functie "print_lijst_van_paginas"
# bijna identiek aan stap 1, alleen nu andere tekst voor als er geen zoekresultaten zijn
#  en ook wordt nu niet enkel de titel maar ook een samenvatting voor elke pagina afgedrukt
def print_lijst_van_paginas(pagina_namen, aantal_paginas, zoekterm):
    if aantal_paginas == 0:
        print("Niks gevonden voor", zoekterm)
    else:
        print("Dit zijn de", str(aantal_paginas), "meest relevante pagina's over", zoekterm + ":")
        nummer = 1
        for pagina_naam in pagina_namen:
          #  druk een volgnummer en de pagina_naam af          
            print(str(nummer) + ". " + pagina_naam)
          #  druk de samenvatting af
            ________________
            nummer = nummer + 1

    print_lege_regel()

# functie "vind_en_print_samenvatting"
# neemt 1 parameter "pagina_naam" en druk de eerste zin van de uitleg af die je via wikipedia vindt
def vind_en_print_samenvatting(pagina_naam):
  # vul variabele met eerste zin van de uitleg
    uitleg = wikipedia.___________
  # druk variabele af
    print(uitleg)
    print_lege_regel()

# functie "zoek_suggestie"
# neemt 1 parameter 'zoekterm' en geeft de suggestie van wikipedia als resultaat
def zoek_suggestie(zoekterm):
    return wikipedia.____________

# functie "vind_en_print_suggestie"
# neemt 1 parameter "zoekterm"
def vind_en_print_suggestie(zoekterm):
  # zoek de suggestie voor de zoekterm
    suggestie = _________
  # als je iets vindt  (dus niet 'none') ...
    if suggestie != None:
      # ... dan drukken we wat tekst af en de paginas voor de suggestie
        print("Niks gevonden voor", zoekterm)
        print_lege_regel()
        print("Maar misschien bedoelde je", suggestie + "?")
        pagina_namen = __________(suggestie)
        print_lijst_van_paginas(pagina_namen, len(pagina_namen), zoekterm)

# hoofdfunctie "wiki"
# lichtjes aangepast tegenover stap 1
def wiki():
    wikipedia.set_lang("nl")
    zoekterm = vraag_zoekterm()
    print_lege_regel()

    while not zoekterm == "<stop>":
        pagina_namen = vind_pagina_namen(zoekterm)
      # bepaal aantal paginas
        aantal_paginas = len(pagina_namen)
      # als er geen paginas zijn
        if aantal_paginas == 0:
          # zoek dan suggestie
            ____________(zoekterm)
        else: 
          # anders druk de gevonden paginas af
            ____________(pagina_namen, aantal_paginas, zoekterm)

        zoekterm = vraag_zoekterm()

wiki()