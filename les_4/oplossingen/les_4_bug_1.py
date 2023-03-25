#functie die de som van 2 getallen maakt
def maaksom(getal1, getal2):
  som = getal1 + getal2
  return som

#2 getallen
x = 2
y = 3
#de som maken
z = maaksom(x, y)

#het resultaat afdrukken
if (z > 4):
  print("Ja, hoor. De som van 2 en 3 is groter dan 4")
else:
  print("Er ging iets mis.")