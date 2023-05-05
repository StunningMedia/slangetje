from collections import Counter

opi_team = [1,2,3,3,3,2,3,2,1,1,2,2,3,3,2,1,3,1,1,3,2,1]
development = [1,2,2,2,1]
sales = [3,1,2,3,3,3,2,3,2,1,1,2,2,3,3,2,1,3,1,1,2,1]

def maak_frequentie_tabel(lijst):
    return dict(Counter(lijst))

def print_frequentie_tabel(lijst):
    print(maak_frequentie_tabel(lijst))

# gesorteerd op aantal keer dat de waarde voorkomt
print_frequentie_tabel(opi_team)
print_frequentie_tabel(development)
print_frequentie_tabel(sales)