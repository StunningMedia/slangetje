# slide 2015820 (Basisbewerkingen - gebruikte dictionaries)
show_alignments = {
    'Agent Carter': 'Lawful Good',
    'The Flash': 'Neutral Good',
    'The Punisher': 'Chaotic Good',
    'Gotham': 'Lawful Neutral',
}

show_alignments2 = dict([
    ('The Umbrella Academy', 'Neutral'),
    ('DC Titans', 'Chaotic Neutral'),
    ('Watchmen', 'Lawful Evil'),
    ('Legion', 'Neutral Evil'),
    ('The Boys', 'Chaotic Evil')
])


#-----------------------------------------------------------------------------------

# slide 2041947 (Basisbewerkingen - items toevoegen of aanpassen)

print('na definitie')
print(show_alignments)
print(show_alignments2)
print('\n')

show_alignments['Green Arrow'] = 'Chaotic Good'


print('na aanmaak Green Arrow')
print(show_alignments)
print(show_alignments2)
print('\n')

show_alignments.update(show_alignments2)


print('na samenvoegen')
print(show_alignments)
print(show_alignments2)
print('\n')

show_alignments['Green Arrow'] = 'Neutral Good'


print('na update green arrow')
print(show_alignments)
print(show_alignments2)
print('\n')
#-----------------------------------------------------------------------------------

# slide 2041948 (Basisbewerkingen - items verwijderen)

del show_alignments['Green Arrow']
# of:
#green_arrow = show_alignments.pop('Green Arrow')

last_item_with_key = show_alignments.popitem()

show_alignments.clear()

del show_alignments


#-----------------------------------------------------------------------------------

# slide 2041950 (Basisbewerkingen - items opvragen)
# print(show_alignments['Green Arrow'])
# print(show_alignments.get('Green Arrow'))

print(show_alignments.get('Joske Vermeulen', 'Neutral'))
# Als de key 'Joske Vermeulen' niet bestaat wordt de waarde 'Neutral' terug gegeven.
print(show_alignments)

# print(show_alignments.setdefault('Joske Vermeulen', 'Neutral'))
# Als de key 'Joske Vermeulen' niet bestaat wordt de waarde 'Neutral' terug gegeven.
# Het verschil met de get-methode is dat de key nu ook toegevoegd is in show_alignment, met de waarde 'Neutral'
# print(show_alignments)


#-----------------------------------------------------------------------------------

# slide 2041949 (Een dictionary overlopen)

for key in show_alignments:
  print(key)

for key in show_alignments:
  print(show_alignments[key])

# sleutels overlopen en afdrukken
for key in show_alignments.keys():
  print(key)

# waarden overlopen en afdrukken
for value in show_alignments.values():
  print(value)

# sleutels & waarden overlopen
for key, value in show_alignments.items():
  print('Sleutel is: ', key, '.  En de waarde is: ', value)
