from collections import Counter

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

tekst = 'OLIEBOLLENKRAAMPJES'
# frequentie_tabel = maak_frequentie_tabel(tekst)
# print(frequentie_tabel) 
# print(sorteer_volgens_frequentie(frequentie_tabel))
print(kuis_tekst_op(vergelijkings_tekst))