from collections import Counter

def maak_frequentie_tabel(tekst):
    return Counter(tekst)

def sorteer_volgens_frequentie(frequentie_tabel):
    meest_voorkomende = frequentie_tabel.most_common()
    frequentie_dictionary = dict(meest_voorkomende)
    frequentie_lijst = list(frequentie_dictionary.keys())
    return frequentie_lijst


tekst = 'OLIEBOLLENKRAAMPJES'
frequentie_tabel = maak_frequentie_tabel(tekst)
print(frequentie_tabel) 
print(sorteer_volgens_frequentie(frequentie_tabel))