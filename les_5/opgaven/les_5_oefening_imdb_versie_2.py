# hier maken we dezelfde oplossing als in versie 1, maar efficiënter geprogrammeerd.  Eerst nadenken en dan programmeren, weet je wel? .... 
# in de commentaar-lijnen bij deze versie bespreken we enkel wat verschillend is t.o.v. versie 1
import imdb
data = imdb.IMDb()

the_matrix = data.get_movie('0133093')
the_fellowship_of_the_ring = data.get_movie('0120737')
a_space_odyssey = data.get_movie('0062622')
the_name_of_the_rose = data.get_movie('0091605')
the_man_with_the_golden_gun = data.get_movie('0071807')

films = [the_matrix, the_fellowship_of_the_ring, a_space_odyssey, the_name_of_the_rose, the_man_with_the_golden_gun]
indentation = "  "

def pas_naam_aan(naam):
    naam = str(naam)
  # hier gebruiken we nu een split commando ipv de positie van de spatie bij te houden in variabele 'pos'
    voornaam, familienaam = naam.split(' ')
    return familienaam + ", " + voornaam

# hier definiëren we een functie 'print_simple_property' die een eenvoudige eigenschap van een film kan afdrukken.
# deze functie heeft 3 parameters:
#    1. film:       de film in kwestie
#    2. name:       met welke label je de eigenschap wil afdrukken
#    3. imdb_name:  met welke naam je die eigenschap moet vragen aan IMDb
def print_simple_property(film, name, imdb_name):
  # druk het label af, gevolgd door een dubbelpunt, gevolgd door de eigenschap zoals je ze aan IMDb vraagt
    print()

# hier definiëren we een functie 'print_list_property' die een lijst-eigenschap van een film kan afdrukken.  
# Deze functie heeft 5 parameters :
#    1. film:         de film in kwestie
#    2. single_name:  met welke label je de eigenschap wil afdrukken als er 1 item in de lijst staat
#    3. multiple_name:  met welke label je de eigenschap wil afdrukken als er meer dan 1 item in de lijst staat
#    4. imdb_name:  met welke naam je die eigenschap moet vragen aan IMDb
#   5. transform_item_function:  welke functie moet toegepast worden om het item afdrukbaar te maken.  Dit is een specialleke:   we geven hier een functie door als een parameter van een andere functie !!
def print_list_property(film, single_name, multiple_name, imdb_name, transform_item_function):
  # eerst zoeken we de eigenschap van de film, gebruikmakend van de imdb_naam van de eigenschap.  Bewaar in variabele 'list_property'
    
  # variabele 'has_more_than_one_entry' zetten we op TRUE als de lijst langer dan 1 is, en anders op false
    
  #  als er meer dan één is drukken we de multiple_name af
    if has_more_than_one_entry:
        print(multiple_name)
    # anders drukken we de single_name af
    else:
        print(single_name)
    # daarna lussen we over alle items in de lijst ...
    for item in list_property:
        # en drukken het resultaat af van wat de transformatie-functie geeft. 
        print(indentation +    )

def print_lege_lijn():
    print()

# hier nog een kleine functie om de acteurs van een film af te drukken, ook weer compleet met titel.
# de enige reden dat we dit ook niet doen met de functie print_list_property, is dat we hier de lijst willen beperken tot 3.  Dat kunnen we niet als we domweg de hele list-property zouden afdrukken.
def print_actors(film):
    print("BELANGRIJKSTE ACTEURS")
    for acteur in :
        print(indentation + )

# de functie druk_film_info_overzicht wordt nu een stuk overzichtelijker:
def druk_film_info_overzicht(films):
  # voor elke film in lijst 'films' ...
    for film in films:
      # druk simpele eigenschap 'titel' af
        
      # druk de regisseurs af.   Regisseurs zijn personen dus we gebruiken als transformatie-functie 'pas_naam_aan'
        
      # druk de genres af.  Hier gebruiken we als transformatie-functie gewoon 'str'
        
      # druk de acteurs af
        
      # en nog een lege lijn
        


# tenslotte de aanroep zelf
druk_film_info_overzicht(films)
