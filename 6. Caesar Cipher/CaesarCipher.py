"""
Szyfr Cezara
Szyfr Cezara jest szyfrem przesuwającym, który używa dodawania i odejmowania,
by szyfrować i odszyfrowywać litery.
Etykiety: krótki, dla początkujących, kryptografia, matematyka
"""

import pyperclip 

print('Szyfr Cezara, autor: Al Sweigart, al@inventwithpython.com')
print('Szyfr Cezara szyfruje litery przez przesunięcie ich o liczbę,')
print('która jest kluczem. Na przykład klucz 2 oznacza, że litera A jest')
print('zamieniona na C, litera B na D i tak dalej.')
print()

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
    print('Czy chcesz (z)aszyfrować, czy (o)dszyfrować?')
    response = input('> ').lower()
    if response.startswith('z'):
        mode = 'zaszyfrowania'
        break
    elif response.startswith('o'):
        mode = 'odszyfrowania'
        break
    print('Proszę podać literę z lub o.')

while True:
    maxKey = len(SYMBOLS) - 1
    print('Proszę podać klucz (0 do {0}).'.format(maxKey)) 
    response = input('> ').upper()

    if not response.isdecimal():
        continue
    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

print('Wpisz wiadomość do {0}.'.format(mode))
message = input('> ')
message = message.upper()

translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)

        if mode == 'zaszyfrowania':
            num = num + key
        elif mode == 'odszyfrowania':
            num = num - key

        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        translated = translated + SYMBOLS[num]
    else:
        translated = translated + symbol

print(translated)

pyperclip.copy(translated)
print('Tekst przekazany do {0} został skopiowany do schowka.'.format(mode))