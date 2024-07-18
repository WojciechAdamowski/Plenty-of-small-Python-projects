"""
Zegar cyfrowy
Wyświetla zegar cyfrowy pokazujący aktualny czas za pomocą cyfr
Plik sevseg.py musi być w tym samym folderze.
Etykiety: króciutki, artystyczny
"""

import sys, time
import sevseg

try: 
    while True:
        print('\n' * 60)

        currentTime = time.localtime()

        hours = '12' if currentTime.tm_hour % 12 == 0 else str(currentTime.tm_hour)
        minutes = str(currentTime.tm_min)
        seconds = str(currentTime.tm_sec)

        # Pobierz łańcuch znaków reprezentujących grafikę cyfry z modułu sevseg:
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # Wyświetl cyfry:
        print(hTopRow    + '     ' + mTopRow    + '     ' + sTopRow)
        print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
        print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)
        print()
        print('Naciśnij Ctrl+C, by wyjść.')

        # Wykonuj pętle, dopóki zmieniają się sekundy:
        while time.localtime().tm_sec == currentTime.tm_sec:
            time.sleep(0.01)
except KeyboardInterrupt:
    print('Zegar cyfrowy')
    sys.exit()  # Po naciśnięciu Ctrl+C zakończ program.