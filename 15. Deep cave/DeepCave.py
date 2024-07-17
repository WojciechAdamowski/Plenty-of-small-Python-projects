"""
Głęboka jaskinia
Animacja głębokiej jaskini, która nieskończenie schodzi w głąb ziemi.
Etykiety: króciutki, dla początkujących, przewijanie, artystyczny
"""

import random, sys, time

WIDTH = 70
PAUSE_AMOUNT = 0.05

print('Głęboka jaskinia')
print('Naciśnij Ctrl+C, by zatrzymać.')
time.sleep(2) 

leftWidth = 20
gapWidth = 10

while True:
    rightWidth = WIDTH - gapWidth - leftWidth
    print(('#' * leftWidth) + (' ' * gapWidth) + ('#' * rightWidth)) 

    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit() 

    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and leftWidth > 1:
        leftWidth = leftWidth - 1 # Zmniejsz szerokość lewej strony.
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
        leftWidth = leftWidth + 1 # Zwiększ szerokość lewej strony.
    else:
        pass

    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and gapWidth > 1:
        gapWidth = gapWidth - 1 # Zmniejsz szerokość przerwy.
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
        gapWidth = gapWidth + 1 # Zwiększ szerokość przerwy.
    else:
        pass

