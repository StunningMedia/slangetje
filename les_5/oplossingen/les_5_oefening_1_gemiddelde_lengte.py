#dit is de lijst die we als input voor de functie gaan gebruiken
vrienden = ["Joshua", "Anna", "Lowie", "Silke", "Wout", "Siebe"]


# hier definiëren we de functie 'gemiddelde_lengte'
# deze functie krijgt een lijst van strings als parameter binnen
def gemiddelde_lengte(lijst_van_strings):
    # eerst totaleLengte op nul zetten
    totaleLengte = 0
    # dan voor elke string in de lijst van strings ...
    for string in lijst_van_strings:
        # bij totaleLengte de lengte van deze string optellen
        totaleLengte += len(string)
        # toon de string
        print(string)
        # toon de lengte van deze string
        print(str(len(string)))
        # toon de nieuwe totale lengte
        print(str(totaleLengte))

    #  tenslotte geven we als resultaat van de functie terug:  de totale lengte gedeeld door het aantal elementen in de lijst van strings
    return int(totaleLengte / len(lijst_van_strings))

# hier roepen we de functie aan zodat we de gemiddelde lengte kunnen afdrukken
print("De gemiddelde lengte van de namen is " + str(gemiddelde_lengte(vrienden)))