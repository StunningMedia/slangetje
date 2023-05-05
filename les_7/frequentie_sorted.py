opi_team = [1,2,3,3,3,2,3,2,1,1,2,2,3,3,2,1,3,1,1,3,2,1]
development = [1,2,2,2,1]
sales = [3,1,2,3,3,3,2,3,2,1,1,2,2,3,3,2,1,3,1,1,2,1]

# nu ook gesorteerd van klein naar groot getal in de lijst

def frequentie_tabel_oplopend(lijst):
    dictionary = {}
    for getal in sorted(lijst):
        dictionary[getal] = dictionary.get(getal, 0) + 1
    return dictionary

def print_frequentie_tabel_oplopend(lijst):
    print(frequentie_tabel_oplopend(lijst))
    print()

print_frequentie_tabel_oplopend(opi_team)
print_frequentie_tabel_oplopend(development)
print_frequentie_tabel_oplopend(sales)