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


def encodeer(tekst, codeersleutel):
    versleutelde_tekst = ''
    
    for letter in tekst:
        versleutelde_tekst += codeersleutel[letter]
    
    return versleutelde_tekst


def print_gecodeerde_tekst(tekst, codeersleutel):
    gecodeerde_tekst = encodeer(tekst, codeersleutel)
    print('Gecodeerde versie van ' + tekst + ' = ' + gecodeerde_tekst)
    print('Gebruikte codeersleutel:')
    print(codeersleutel)

codeersleutel = genereer_willekeurige_codeersleutel()
print_gecodeerde_tekst('ENIGMA', codeersleutel)
