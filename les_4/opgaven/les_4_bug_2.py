#functie die de som maakt van getal1 en 2 keer getal2
def bereken(getal1, getal2):
  return getal1 + getal2 * 2

#2 getallen laten ingeven
x = input("getal 1: ")
y = input("getal 2: ")

#de berekende waarde afdrukken
antwoord = bereken(x, y)
print('Het antwoord is : ' + antwoord)