"""
Odliczanie
Animacja odliczania do zera za pomocą cyfr w stylu wyświetlacza siedmiosegmentowego.
Naciśnij Ctrl+C, by zatrzymać.
Moduł sevseg.py musi być w tym samym folderze.
Etykiety: króciutki, artystyczny
""" 

import sys, time
import sevseg

secondsLeft = 30

try:
    while True:
        print('\n' * 60)

        hours = str(secondsLeft // 3600)
        minutes = str((secondsLeft % 3600) // 60)
        seconds = str(secondsLeft % 60)

        hDigits = sevseg.getSevSegStr(hours, 2)
        mDigits = sevseg.getSevSegStr(minutes, 2)
        sDigits = sevseg.getSevSegStr(seconds, 2)

        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines() 

        print(hTopRow    + '   ' + mTopRow    + '   ' + sTopRow)
        print(hMiddleRow + ' * ' + mMiddleRow + ' * ' + sMiddleRow)
        print(hBottomRow + ' * ' + mBottomRow + ' * ' + sBottomRow)

        if secondsLeft == 0:
            print()
            print(' * * * * BUM * * * *')
            break

        print()
        print('Naciśnij Ctrl+C, by zatrzymać program.') 

        time.sleep(1) # Zrób jednosekundową pauzę.
        secondsLeft -= 1 

except KeyboardInterrupt:
    print('Odliczanie')
    sys.exit()

