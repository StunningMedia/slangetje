opi_team = [1,2,3,3,3,2,3,2,1,1,2,2,3,3,2,1,3,1,1,3,2,1]
development = [1,2,2,2,1]
sales = [3,1,2,3,3,3,2,3,2,1,1,2,2,3,3,2,1,3,1,1,2,1]

def frequentie_tabel(lijst):
    dictionary = {}
    for getal in lijst:
        dictionary[getal] = dictionary.get(getal, 0) + 1
    return dictionary

def print_frequentie_tabel(lijst):
    print(frequentie_tabel(lijst))
    print()

print_frequentie_tabel(opi_team)
print_frequentie_tabel(development)
print_frequentie_tabel(sales)