#functie die 2 getallen vergelijkt
def vergelijk(getal1, getal2):
 #de 2 waardes afdrukken
 print("We gaan " + str(getal1) + " en " + str(getal2) + " vergelijken.")
 if (getal1 > getal2) :
  print(getal1, end="", flush=True)
  print(" is groter dan ", end="", flush=True)
  print(getal2, end="", flush=True)
 elif (getal1 < getal2) :
  print(getal1, end="", flush=True)
  print(" is kleiner dan ", end="", flush=True)
  print(getal2, end="", flush=True)
 else :
  print(getal2, end="", flush=True)
  print(" is gelijk aan ", end="", flush=True)
  print(getal1)

#2 getallen laten ingeven
x = int(input("getal 1: "))
y = int(input("getal 2: "))

#de waardes vergelijken
vergelijk(x, y)