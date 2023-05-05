import os


import pygame
pygame.init()

def vraag_bestandsnaam():
  naam_bestand = input("Bestand: ")
  return naam_bestand


def laad_bestand(naam_bestand, script_pad):
  relatief_pad = "tekstbestanden/" + naam_bestand + ".txt"
  bestands_pad = os.path.join(script_pad, relatief_pad)
  bestand = open(bestands_pad, "r")
  return bestand
  

def start_programma():
  gebruiker_wil_doorgaan = True
  stopzin = "no more, for the love of God and all that is Holy: NO MORE!"
  script_folder = os.path.dirname(__file__) # folder waar het script wordt uitgevoerd

  # eerste keer gewoon een bestand vragen
  print("Welk bestand wil je openen?  Enkel bestanden uit de map 'tekstbestanden' zijn toegestaan.")
  naam_bestand = vraag_bestandsnaam()
  bestand = laad_bestand(naam_bestand, script_folder)

  # erna een conditionele lus
  while gebruiker_wil_doorgaan:
    transformeer_bestand(bestand, naam_bestand)
    print_menu(stopzin)
    naam_bestand = vraag_bestandsnaam()
    gebruiker_wil_doorgaan = wil_gebruiker_doorgaan(naam_bestand, stopzin)
    if gebruiker_wil_doorgaan:
      print('Transformatie begint')
      bestand = laad_bestand(naam_bestand, script_folder)
    else:
      print()
      print('Aangenaam werken met u, tot de volgende keer!')


def transformeer_bestand(bestand, naam_bestand):
  tekst_array = []
  for lijn in bestand:
    tekst_array.append(lijn)
  
  aantal_lijnen_tekst = len(tekst_array)
  aantal_tekens_eerste_lijn = len(tekst_array[0])
  hoogte = aantal_lijnen_tekst
  breedte = aantal_tekens_eerste_lijn

  afbeelding = pygame.Surface((breedte, hoogte))
  pixel_array = pygame.PixelArray(afbeelding)

  voeg_gekleurde_pixels_toe(tekst_array, pixel_array, hoogte, breedte)
  sla_op_als_jpg(bestand, naam_bestand, afbeelding)



def sla_op_als_jpg(bestand, naam_bestand, afbeelding):
  bestand.close()
  naam_resultaat = naam_bestand + ".jpg"
  pygame.image.save(afbeelding, naam_resultaat)
  print("Klaar!  Bekijk " + naam_resultaat)


def voeg_gekleurde_pixels_toe(tekst_array, pixel_array, hoogte, breedte):
  klinkers = "aeiou"

  for lijn_index in range(hoogte):
    lijn = tekst_array[lijn_index]
    for letter_index in range(breedte):
      if lijn[letter_index] in klinkers:
        pixel_array[letter_index, lijn_index] = (0, 0, 0)
      else:
        pixel_array[letter_index, lijn_index] = (255, 255, 255)

  pixel_array.close()



def sluit_bestand(bestand):
  bestand.close()


def wil_gebruiker_doorgaan(naam_bestand, stopzin):
  if naam_bestand == stopzin:
    return False

    # Dit gebeurt enkel als de gebruiker wil doorgaan
  return True


def print_menu(stopzin):
  print('U heeft twee keuzes:')
  print("1. Kies een bestand uit de map tekstbestanden en transformeer het (u ziet de output in de console")
  print("2. U wil stoppen met dit spelletje: geef dan als bestandsnaam volgende stopzin in: '" + stopzin + "'")


start_programma()