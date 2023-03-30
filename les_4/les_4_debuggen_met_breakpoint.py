import os

# de lijn hieronder dient om de breakpoints af te zetten
# als je deze lijn in commentaar zet heb je WEL de breakpoints
# als je deze lijn uit commentaar haalt krijg je NIET de breakpoints
os.environ['PYTHONBREAKPOINT'] = '0'

#functie die een waarde berekent op basis van 2 getallen
def bereken(x, y):
  y = y**2
  x *= 2
  z = x + y
  return z

#4 variabelen
z = 5
x = 50
y = 60
n = 1000

#hier komt een breakpoint
breakpoint()

#eerste berekening
bereken(5, 10)
print('z = ' + str(z))

#tweede berekening
n = bereken(2, 3)
print('n = ' + str(n))