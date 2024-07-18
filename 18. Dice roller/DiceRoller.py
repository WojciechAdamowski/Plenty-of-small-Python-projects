"""
Rzut kostką, autor
Program symuluje rzuty kostką według notacji Dungeons & Dragons.
Etykiety: krótki, symulacja
"""

import random, sys

print('''Rzut kostką

Wpisz iloma i jakimi kościami chcesz rzucić. Zapis to liczba kości,
potem "d", a potem liczba ścianek tych kości.
Możesz również dodać lub odjąć oczka od sumy wyrzuconych punktów.

Przykłady:
  3d6 to rzut trzema sześciennymi kostkami
  1d10+2 to rzut jedną 10-ścienną kostką i dodanie 2 oczek
  2d38-1 to rzut dwoma 38-ściennymi kostkami i odjęcie 1 oczka
  KONIEC kończy program
''')

while True:
    try:
        diceStr = input('> ')

        if diceStr.upper() == 'KONIEC':
            print('Dziękujemy za grę!')
            sys.exit()

        diceStr = diceStr.lower().replace(' ','')

        dIndex = diceStr.find('d')
        if dIndex == -1:
            raise Exception('Brakuje litery "d".')
        
        numberOfDice = diceStr[:dIndex]
        if not numberOfDice.isdecimal():
            raise Exception('Brakuje liczby kostek.')
        numberOfDice = int(numberOfDice)

        modIndex = diceStr.find('+')
        if modIndex == -1:
            modIndex = diceStr.find('-')

        if modIndex == -1:
            numberOfSides = diceStr[dIndex + 1 :]
        else:
            numberOfSides = diceStr[dIndex + 1 : modIndex]

        if not numberOfSides.isdecimal():
            raise Exception('Brakuje liczby ścianek.')
        numberOfSides = int(numberOfSides)

        if modIndex == -1:
            modAmount = 0
        else:
            modAmount = int(diceStr[modIndex + 1 :])
            if diceStr[modIndex] == '-':
                modAmount = -modAmount

        rolls = []
        for i in range(numberOfDice):
            rollResult = random.randint(1, numberOfSides)
            rolls.append(rollResult)

        print('Suma:', sum(rolls) + modAmount, '(Każda kostka ', end='')

        # Wyświetl poszczególne rzuty:
        for i, roll in enumerate(rolls):
            rolls[i] = str(roll)
        print(', '.join(rolls), end='')

        # Wyświetl wartość modyfikatora:
        if modAmount != 0:
            modSign = diceStr[modIndex]
            print(', {}{}'.format(modSign, abs(modAmount)), end='')
        print(')')



    except Exception as exc:
        # W razie błędu, wyświetl informację użytkownikowi:
        print('Zapis rzutu w niepoprawnym formacie. Wpisz coś w stylu "3d6" lub "1d10+2".')
        print('Powód niepoprawnego zapisu: ' + str(exc))
        continue  # Wróć do pytania o rzut.
