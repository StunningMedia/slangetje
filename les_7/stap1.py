import random

alfabet = [
    'A', 'B', 'C', 'D', 'E',
    'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y',
    'Z'
]

def genereer_willekeurige_codeersleutel():
    codeersleutel = {}

    for letter in alfabet:
        codeersleutel[letter] = krijg_willekeurige_letter(codeersleutel.values())

    return codeersleutel

def krijg_willekeurige_letter(reeds_gebruikte_letters):
    willekeurige_letter = alfabet[random.randint(0, 25)]
    
    while willekeurige_letter in reeds_gebruikte_letters:
        willekeurige_letter = alfabet[random.randint(0, 25)]
    
    return willekeurige_letter


print(genereer_willekeurige_codeersleutel())