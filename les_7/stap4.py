from collections import Counter

def maak_frequentie_tabel(tekst):
    return dict(Counter(tekst))

tekst = 'OLIEBOLLENKRAAMPJES'
frequentie_tabel = maak_frequentie_tabel(tekst)
print(frequentie_tabel)
