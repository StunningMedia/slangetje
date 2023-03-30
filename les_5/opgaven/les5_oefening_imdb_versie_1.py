# eerst importeren we library "imdb"
import imdb
# en we stoppen dan zo'n IMDb-instance in variabele 'data'
data = imdb.IMDb()
# vanaf nu kunnen we aan 'data' alles vragen

# eerst zoeken we een paar films op
the_matrix = data.get_movie('0133093')
the_fellowship_of_the_ring = data.get_movie('0120737')
a_space_odyssey = data.get_movie('0062622')
the_name_of_the_rose = data.get_movie('0091605')
the_man_with_the_golden_gun = data.get_movie('0071807')

# en dan stoppen we al die gevonden films in een lijst 'films'
films = [the_matrix, the_fellowship_of_the_ring, a_space_odyssey, the_name_of_the_rose, the_man_with_the_golden_gun]
indentation = "  "

# definieer hier een functie 'pas_naam_aan' om voornaam en familienaam om te draaien, en met een komma ertussen
def pas_naam_aan(person):
  # vul een variabele 'naam' met de naam van de persoon
    naam = 
  # zoek de positie van de spatie tussen voor- en achternaam
    pos = 
  # voornaam is alles voor de spatie
    voornaam = 
  # achternaam is alles na de spatie
    familienaam = 
  # plak netjes aan elkaar met komma ertussen en geef resultaat
    return 

# definieer een functie om een lege lijn af te drukken
def print_lege_lijn():
    print()

# definieer een functie om alle info van alle films af te drukken
def druk_film_info_overzicht(films):
  # voor elke film in lijst 'films' ....
    for film in films:
      # druk de titel af
        print("TITEL : ", )

      # nu gaan we de regisseur(s) info afdrukken
      # als er meer dan 1 regisseur is, druk dan het woord "REGISSEURS" af
        if len(film['directors']) > 1:
            print("REGISSEURS")
      # anders, als er maar 1 regisseur is, druk dan het woord "REGISSEUR" af
        else:
            print("REGISSEUR")
      # voor elke regisseur die je terugkrijgt door lijst film['directors'] op te vragen ...
        for regisseur in :
          #  druk de aangepaste naam van deze persoon af
            print(indentation + )

      # nu drukken we de genre(s) informatie af, op dezelfde manier als voor de regisseurs    
      # eerst de juiste titel afhankelijk van enkelvoud of meervoud
        if len(film['genres']) > 1:
            print("GENRES")
        else:
            print("GENRE")
      # en dan alle genres één voor één afdrukken
      # let erop dat je een genre niet zomaar kan afdrukken, je moet het eerst omvormen naar een string!
        for genre in film['genres']:
            print(indentation + )

     # tenslotte nog de lijst van belangrijkste acteurs.  Dit is altijd meervoud dus geen selectie nodig    
        print("BELANGRIJKSTE ACTEURS")
      # we beperken de lijst tot maximaal 3 acteurs, en drukken dan voor elke acteur in de top-3 de aangepaste naam af
        for acteur in film['cast'][:3]:
            print(indentation + )

      #tenslotte nog een lege lijn zodat duidelijk is waar de volgende film z'n  informatie begint
        print_lege_lijn()
# einde functie 'druk_film_info_overzicht'

# nu alles opgezocht is, en de functies die we nodig hebben gedefinieerd zijn, kunnen we de hoofd-functie aanroepen met als parameter de lijst van onze opgezochte films
druk_film_info_overzicht(films)