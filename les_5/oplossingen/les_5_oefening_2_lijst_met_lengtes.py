#  dit is de lijst die we als invoer gaan gebruiken
vrienden = ["Joshua", "Anna", "Lowie", "Silke", "Wout", "Siebe"]
# die drukken we al even af
print("Lijst met de namen = ", vrienden)


# we maken een functie 'lijst_met_naam_lengtes' 
#    die een lijst als parameter aanneemt
def lijst_met_naam_lengtes(lijst_met_namen):
    # maak een nieuwe, lege lijst genaamd 'lijst_met_lengtes'
    lijst_met_lengtes = []
    # voor elke naam in lijst_met_namen ...
    for naam in lijst_met_namen:
        # pak de lengte van de naam en voeg die toe aan lijst_met_lengtes
        lijst_met_lengtes.append(len(naam))
    # geef lijst_met_lengtes terug als functie resultaat
    return lijst_met_lengtes


# hier de aanroep om de functie uit te voeren
print("Lijst met de lengtes van de namen = ", lijst_met_naam_lengtes(vrienden))