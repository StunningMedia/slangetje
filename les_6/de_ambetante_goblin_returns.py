nieuwe_lijn = '\n'
lijn_witruimte = nieuwe_lijn + nieuwe_lijn

def vraag_wachtwoord():
    return input(nieuwe_lijn + "HALT! Wat is het wachtwoord?" + nieuwe_lijn)

def ambetante_goblin(wachtwoord):
    wachtwoord_poging = vraag_wachtwoord()
    lengte_wachtwoord = len(wachtwoord_poging)

    if wachtwoord_poging == wachtwoord:
        return False # hierdoor stopt de lus & deze methode

    # dit gebeurt enkel als het wachtwoord fout was
    print(wachtwoord_poging * lengte_wachtwoord)
    return True

def brave_goblin(wachtwoord):
    eind_tekst = '''
De goblin laat zijn pijl en boog zakken, trekt zijn broek weer naar omhoog & laat je erdoor.

"Veel plezier in Moria!"        
'''
    print(wachtwoord + ' is inderdaad het juiste wachtwoord.' + lijn_witruimte + eind_tekst)

def start():
    intro_text = """
Je komt aan een touwbrug over een diep ravijn.  In het midden staat een goblin.
Als je op de touwbrug stapt, toont hij eerst zijn bloot gat, kakelt van het lachen & neemt dan een boog en richt een pijl op jou.
"""
    print(intro_text + nieuwe_lijn)

def run_ambetante_goblin_programma():
    wachtwoord = 'goblin is groot, goblin is machtig'
    goblin_doet_ambetant = True

    start()

    while goblin_doet_ambetant:
        goblin_doet_ambetant = ambetante_goblin(wachtwoord)
    
    brave_goblin(wachtwoord)

run_ambetante_goblin_programma()