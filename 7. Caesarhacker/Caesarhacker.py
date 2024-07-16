"""
Łamacz szyfru Cezara
Ten program odtajnia wiadomości zaszyfrowane przy użyciu szyfru Cezara
za pomocą ataku brute force sprawdzającego każdy możliwy klucz.
Etykiety: króciutki, dla początkujących, kryptografia, matematyka
"""

print('Łamacz szyfru Cezara')

print('Wpisz wiadomość zaszyfrowaną szyfrem Cezara, którą chcesz odtajnić.')
message = input('> ')

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)):
    translated = ''

    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            num = num - key

            if num < 0:
                num = num + len(SYMBOLS)

            translated = translated + SYMBOLS[num]
        else:
            translated = translated + symbol

    print('Klucz #{}: {}'.format(key, translated))