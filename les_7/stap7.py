from collections import Counter, OrderedDict
import random

alfabet = [
    'A', 'B', 'C', 'D', 'E',
    'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y',
    'Z'
]

def genereer_willekeurige_codeersleutel():
    codeersleutel = {}

    for letter in alfabet:
        codeersleutel[letter] = krijg_willekeurige_letter(codeersleutel.values())

    return codeersleutel


def sorteer_codeersleutel(codeersleutel):
    return dict(OrderedDict(sorted(codeersleutel.items())))

def vergelijk_codeersleutels(sleutel1, sleutel2):
    print(sorteer_codeersleutel(sleutel1))
    print(sorteer_codeersleutel(sleutel2))
    print('de twee sleutels zijn gelijk: ' + str(sleutel1 == sleutel2))

def krijg_willekeurige_letter(reeds_gebruikte_letters):
    willekeurige_letter = alfabet[random.randint(0, 25)]
    
    while willekeurige_letter in reeds_gebruikte_letters:
        willekeurige_letter = alfabet[random.randint(0, 25)]
    
    return willekeurige_letter


def encodeer(tekst, codeersleutel):
    versleutelde_tekst = ''
    
    for letter in tekst:
        versleutelde_tekst += codeersleutel[letter]
    
    return versleutelde_tekst


def print_gecodeerde_tekst(tekst, gecodeerde_tekst, codeersleutel):
    print('Gecodeerde versie van ' + tekst + ' = ' + gecodeerde_tekst)
    print('Gebruikte codeersleutel:')
    print(codeersleutel)

def decodeer(versleutelde_tekst, codeersleutel):
    decodeersleutel = {}

    for key in codeersleutel.keys():
        decodeer_key = codeersleutel[key]
        decodeersleutel[decodeer_key] = key

    return encodeer(versleutelde_tekst, decodeersleutel)

def print_gedecodeerde_tekst(versleutelde_tekst, codeersleutel):
    print('Gedecodeerde versie van ' + versleutelde_tekst + ' = ' + decodeer(versleutelde_tekst, codeersleutel))

def maak_frequentie_tabel(tekst):
    return Counter(tekst)

def sorteer_volgens_frequentie(frequentie_tabel):
    meest_voorkomende = frequentie_tabel.most_common()
    frequentie_dictionary = dict(meest_voorkomende)
    frequentie_lijst = list(frequentie_dictionary.keys())
    return frequentie_lijst

vergelijkings_tekst = """
Op de oevers langs de Dijle in Leuven, maar ook langs andere waterlopen,
kan je tomatenplanten, pompoenen, kiwiplanten en zelfs vijgenbomen terugvinden. 
De planten groeien uit de zaden die via de riolering op het slib langs de
oevers worden afgezet, daarom worden ze wel eens toiletplanten genoemd. Met 
dank aan het rioolwater dat in de Dijle belandt, vind je langs de oevers in 
Leuven soms verrassende begroeiing zoals tomaten-, pompoenen- en kiwiplanten 
tot zelfs een vijgenboom. Dat schrijft het studentenblad Veto en wordt ons 
bevestigd door Thomas Gyselinck, praktijkassistent biologie aan de KU Leuven:
Van goudbes en tomaat weten we dat ze in ons verteringsstelsel kunnen overleven.
Dat betekent dat als iemand tomaat eet en hij of zij naar de wc gaat, de
zaden via het toilet het water inkomen. Wanneer dat rioleringswater in onze 
waterlopen terechtkomt, worden die zaden meegevoerd en kunnen ze zich 
handhaven op slibafzetting langs het water.Op het slib en via spleten in
muren kunnen de planten groeien. Het stedelijk klimaat, dat altijd enkele graden 
warmer is dan daarbuiten, kan die soorten helpen te bloeien, aldus Thomas 
Gyselinck. In het Groot Begijnhof zijn er kiwiplanten en met een beetje geluk 
pompoenplanten te vinden. In het Sluispark staat er een gigantische vijgenboom 
en naast de zandhopen daar niet ver vandaan staan een heleboel tomatenplanten 
en kun je zelfs goudbes vinden. De planten vinden dus via de riolering nieuwe 
plaatsen om te groeien, maar dat betekent ook dat er nog steeds rioleringswater 
in onze waterlopen terechtkomt. Wanneer we in ons rioleringsstelsel te veel water 
op een korte periode krijgen, namelijk bij zware regenval, dan gebeurt het dat het 
teveel aan water afgeleid wordt naar waterlopen. In Leuven zijn er bovendien nog 
altijd afwateringsbuizen van huizen die rechtstreeks aangesloten zijn op de 
waterlopen. Qua probleem kan dat tellen, zei een ex-medewerker van de 
watermaatschappij ons gisteren.
"""

def kuis_tekst_op(tekst):
    opgekuiste_tekst = ''

    for teken in tekst:
        if(teken.isalpha()):
            opgekuiste_tekst += teken

    return opgekuiste_tekst.upper()


def leer_code(gecodeerde_opgekuiste_tekst, echte_opgekuiste_tekst):
  frequentie_tabel_echte_tekst = maak_frequentie_tabel(echte_opgekuiste_tekst)
  frequentie_lijst_echte_tekst = sorteer_volgens_frequentie(frequentie_tabel_echte_tekst)
  frequentie_tabel_gecodeerde_tekst = maak_frequentie_tabel(gecodeerde_opgekuiste_tekst)
  frequentie_lijst_gecodeerde_tekst = sorteer_volgens_frequentie(frequentie_tabel_gecodeerde_tekst)
  
  codeersleutel_om_te_decoderen = {}
  positie = 0

  while positie < 26:
    codeersleutel_om_te_decoderen[frequentie_lijst_echte_tekst[positie]] = frequentie_lijst_gecodeerde_tekst[positie]
    positie = positie + 1
  
  return codeersleutel_om_te_decoderen

codeersleutel = genereer_willekeurige_codeersleutel()
print("Originele code = ", codeersleutel)
opgekuiste_tekst = kuis_tekst_op(vergelijkings_tekst)
gecodeerde_tekst = encodeer(opgekuiste_tekst, codeersleutel)
vermoedelijke_codeersleutel = leer_code(gecodeerde_tekst, opgekuiste_tekst)
print("Berekende code = ", vermoedelijke_codeersleutel)
print(decodeer(gecodeerde_tekst, vermoedelijke_codeersleutel))

vergelijk_codeersleutels(codeersleutel, vermoedelijke_codeersleutel)

