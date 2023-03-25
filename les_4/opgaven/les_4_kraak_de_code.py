import random

#functie om een opgave te genereren
def genereerOpgave() :
  opgave = str(random.randint(1, 3))
  opgave = opgave + str(random.randint(1, 3))
  opgave = opgave + str(random.randint(1, 3))
  opgave = opgave + str(random.randint(1, 3))
  opgave = opgave + str(random.randint(1, 3))
  opgave = opgave + str(random.randint(1, 3))
  return opgave

#de eerste test
def test1() :
  a = int(input("a = "))
  b = int(input("b = "))
  if a == b :
    return "1"
  elif a > b :
    return "2"
  else :
    return "3"

#de tweede test
def test2() :
  a = int(input("a = "))
  b = int(input("b = "))
  c = int(input("c = "))
  if a == b and not (c > 3) :
    return "1"
  elif a == b and not (c >= 5) :
    return "2"
  else :
    return "3"

#de derde test
def test3() :
  a = input("a = ")
  b = int(input("b = "))
  c = int(input("c = "))
  if a == "a" and b == c :
    return "1"
  elif b == c :
    return "2"
  else :
    return "3"

#de vierde test
def test4() :
  a = int(input("a = "))
  b = int(input("b = "))
  c = int(input("c = "))
  d = int(input("d = "))
  if a * b > 5 and a + c > d :
    return "1"
  elif a * b > 5 or a + c > d :
    return "2"
  else :
    return "3"

#de vijfde test
def test5() :
  a = int(input("a = "))
  b = int(input("b = "))
  if a * b > a + b :
    return "1"
  elif a * b == a + b :
    return "2"
  else :
    return "3"

#de zesde test
def test6() :
  a = input("a = ")
  b = int(input("b = "))
  if a == "Ik ben een superprogrammeur" and b > 5 :
    return "1"
  elif a == "Ik ben een superprogrammeur" and b != 5 :
    return "2"
  elif a == "Programmeren is cool":
    return "3"
  else :
    return "0"

#een opgave genereren
opgave = genereerOpgave()
#aankondiging
print("Welkom bij \"KRAAK DE CODE\"")
print("Dit is de opgave: " + opgave)
#het resultaat
resultaat = test1()
resultaat = resultaat + test2()
resultaat = resultaat + test3()
resultaat = resultaat + test4()
resultaat = resultaat + test5()
resultaat = resultaat + test6()
#het resultaat afdrukken
print(resultaat)
#nagaan of het resultaat correct is
if (resultaat == opgave) :
  print("Dat is helemaal juist!")
else :
  print("Dat is niet helemaal juist ...")