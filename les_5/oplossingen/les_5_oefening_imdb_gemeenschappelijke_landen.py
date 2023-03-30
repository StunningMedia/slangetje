# in dit voorbeeld wordt getoond hoe je vlot twee lijsten kan vergelijken, en er de gemeenschappelijke dingen uithalen.

# zorg dat je kan werken met de imdb library, zoals in vorige oefeningen
import imdb
data = imdb.IMDb()

# zoek enkele films
the_matrix = data.get_movie('0133093')
the_fellowship_of_the_ring = data.get_movie('0120737')
a_space_odyssey = data.get_movie('0062622')
the_name_of_the_rose = data.get_movie('0091605')
the_man_with_the_golden_gun = data.get_movie('0071807')

# definieer hier een functie 'gemeenschappelijke_landen' die als parameters twee films neemt
def gemeenschappelijke_landen(film1, film2):
  # we beginnen met een lege lijst in variabele 'gemeenschappelijke_landen'
    gemeenschappelijke_landen = []
  # pak van beide films de lijst landen  (eigenschap 'countries') en bewaar in variabelen 'landen1' en 'landen2'
    landen1 = film1['countries']
    landen2 = film2['countries']
  # voor elk land in landen1 ...
    for land in landen1:
      #  als het land voorkomt in landen2 ...
        if land in landen2:
            # dan voeg het toe aan lijst gemeenschappelijke_landen
            gemeenschappelijke_landen.append(land)
    # geef de gevonden lijst terug als resultaat van de functie
    return gemeenschappelijke_landen
# einde functie gemeenschappelijke_landen

# definieer hier een functie 'toon_gemeenschappelijke_landen' die als parameters twee films neemt
def toon_gemeenschappelijke_landen(film1,film2):
    # bereken de lijst voor de twee films
    gemeenschappelijke_landen_lijst = gemeenschappelijke_landen(film1,film2)

    # druk een lijn tekst af waarin de lijst wordt getoond
    print('Gemeenschappelijke landen voor films "' + film1['title'] + '"','en','"'+film2['title']+'"',  ':' , gemeenschappelijke_landen_lijst)
# einde functie toon_gemeenschappelijke_landen

#  en dan hier een paar aanroepen van toon_gemeenschappelijke_landen
toon_gemeenschappelijke_landen(the_fellowship_of_the_ring,the_matrix)
toon_gemeenschappelijke_landen(a_space_odyssey, the_man_with_the_golden_gun)
toon_gemeenschappelijke_landen(the_fellowship_of_the_ring, the_name_of_the_rose)