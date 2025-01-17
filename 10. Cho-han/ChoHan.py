"""
Cho-han
Tradycyjna japońska gra w kości.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: krótki, dla początkujących, gra
"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'} 

print('''
Cho-Han

W tej tradycyjnej japońskiej grze w kości siedzący na podłodze
krupier potrząsa dwiema kostkami w bambusowym kubku.
Gracz musi odgadnąć, czy wypadnie liczba parzysta (cho), czy nieparzysta (han).
''') 

purse = 5000

while True:

    print('Masz', purse, 'monet. Ile chcesz postawić? (lub KONIEC)')

    while True:
        pot = input('> ')

        if pot.upper() == 'KONIEC':
            print('Dziękujemy za grę!')
            sys.exit() 
        elif not pot.isdecimal():
            print('Podaj kwotę.')
        elif int(pot) > purse:
            print('Nie masz tylu monet')
        else:
            pot = int(pot)
            break
    
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    print('Krupier potrząsa kubkiem i słyszysz dźwięk kości.')
    print('Krupier stawia kubek do góry dnem na podłodze')
    print('i pyta, co obstawiasz.')
    print()
    print(' CHO (parzyste) lub HAN (nieparzyste)?') 

    while True:
        bet = input('> ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Proszę podać "CHO" lub "HAN".')
            continue
        else:
            break

    print('Krupier podnosi kubek:')
    print(' ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print(' ', dice1, '-', dice2) 

    rollsEven = (dice1 + dice2) % 2 == 0

    if rollsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    if playerWon:
        print('Wygrałeś! Zabierasz', pot, 'monet.')
        purse = purse + pot
        print('Dom hazardowy pobiera opłatę w wysokości ', pot // 10, 'monet.')
        purse = purse - (pot // 10) # Opłata dla domu hazardowego to 10%.
    else:
        purse = purse - pot
        print('Przegrałeś!')
    
    
    if purse == 0:
        print('Nie masz już więcej pieniędzy!')
        print('Dziękujemy za grę!')
        sys.exit()



