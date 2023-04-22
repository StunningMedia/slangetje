nieuwe_lijn = '\n'
lijn_witruimte = nieuwe_lijn + nieuwe_lijn

def vraag_wachtwoord():
    return input(nieuwe_lijn + "HALT! Wat is het wachtwoord?" + nieuwe_lijn)

def ambetante_goblin():
    wachtwoord_poging = vraag_wachtwoord()
    lengte_wachtwoord = len(wachtwoord_poging)

    print(wachtwoord_poging * lengte_wachtwoord)

def brave_goblin():
    laatste_wachtwoord = vraag_wachtwoord()
    eind_tekst = '''
De goblin laat zijn pijl en boog zakken, trekt zijn broek weer naar omhoog & laat je erdoor.

"Veel plezier in Moria!"        
'''

    print(laatste_wachtwoord + ' is inderdaad het juiste wachtwoord.' + lijn_witruimte + eind_tekst)

def start():
    intro_text = """
Je komt aan een touwbrug over een diep ravijn.  In het midden staat een goblin.
Als je op de touwbrug stapt, toont hij eerst zijn bloot gat, kakelt van het lachen & neemt dan een boog en richt een pijl op jou.
"""
    print(intro_text + nieuwe_lijn)
    ambetante_goblin()

def run_ambetante_goblin_programma():
    start()
    ambetante_goblin()
    ambetante_goblin()
    ambetante_goblin()
    brave_goblin()

run_ambetante_goblin_programma()