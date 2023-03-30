import os

vrienden = ["Joshua", "Anna", "Lowie", "Silke", "Wout", "Siebe"]

# elke naam afdrukken samen met de lengte, via een for-lus
for naam in vrienden:
  print(naam)
  print(len(naam))

# lijst in 1 keer afdrukken
print(vrienden)

breakpoint()

# Griet mag ook meespelen
vrienden.append("Griet")

# Wout krijgt een time-out
vrienden.remove("Wout")


# elke naam afdrukken samen met de lengte, via een for-lus
for naam in vrienden:
  print(naam)
  print(len(naam))

# lijst in 1 keer afdrukken
print(vrienden)