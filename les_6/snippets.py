# slide 2041243 (De conditionele lus)

while conditie:
  # code om uit te voeren

#-----------------------------------------------------------------------------------

# slide 2041245 (Wachters & Booleans)

running = True
while running:
  naam = input("naam : ")
  
  if naam == "":
    running = False
  
  for i in range(5):
    print("Hallo",naam)

#-----------------------------------------------------------------------------------

# slide 2041280 (Or just break things!)

while True:
  naam = input("naam : ")
  
  if naam == "":
    break
  
  for i in range(5):
    print("Hallo",naam)

#-----------------------------------------------------------------------------------

# slide 2041247 (Koffers die bij elkaar passen)

match variabele:
  case 'eerste mogelijkheid':
    # code om uit te voeren als de waarde == 'eerste mogelijkheid'
  case 'tweede mogelijkheid' | 'derde mogelijkheid':
    # code om uit te voeren als de waarde == 'tweede mogelijkheid' OF de waarde == 'derde  mogelijkheid'
  case 'xxx':
    # code om uit te voeren als de waarde == 'xxx'
  case _:
    # code om uit te voeren als de waarde niet overeenkomt met één van de andere cases

#-----------------------------------------------------------------------------------

# slide 2041246 (Maar waarom?)

def alarm(item):
  match item:
    case [time, action]:
      print(f'Good {time}! It is time to {action}!')
    case [time, *actions]:
      print('Good morning!')
      for action in actions:
        print(f'It is time to {action}!')

alarm(['afternoon', 'work'])
alarm(('morning', 'have breakfast', 'brush teeth', 'work'))

#-----------------------------------------------------------------------------------

# slide 2041251 (Letterspaghetti: startcode)

import os

# bestand opvragen
def vraag_bestandsnaam():
  naam_bestand = input("Bestand: ")
  return naam_bestand

# code om een bestand uit de subfolder tekstbestanden in te laden
def laad_bestand(naam_bestand, script_pad):
  relatief_pad = "tekstbestanden/" + naam_bestand + ".txt"
  bestands_pad = os.path.join(script_pad, relatief_pad)
  bestand = open(bestands_pad, "r")
  return bestand

# begin van het programma, hier binnen zal je moeten verder werken!
def start_programma():
  gebruiker_wil_doorgaan = True
  stopzin = "no more, for the love of God and all that is Holy: NO MORE!"
  script_folder = os.path.dirname(__file__) # folder waar het script wordt uitgevoerd

  # eerste keer gewoon een bestand vragen
  print("Welk bestand wil je openen?  Enkel bestanden uit de map 'tekstbestanden' zijn toegestaan.")
  naam_bestand = vraag_bestandsnaam()
  bestand = laad_bestand(naam_bestand, script_folder)

#-----------------------------------------------------------------------------------

# slide 2041263 (Pygame)

import pygame
pygame.init()
        
