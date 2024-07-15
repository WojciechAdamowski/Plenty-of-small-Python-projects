"""
Bitmapowa wiadomość
Wyświetla wiadomość tekstową zgodnie z określoną bitmapą.
Etykiety: króciutki, dla początkujących, artystyczny
"""

import sys

bitmap = open('.\\3. Bitmap\\Bitmap.txt', 'r').read()

print('Bitmapowa wiadomość')
print('Wpisz wiadomość, którą chcesz wyświetlić w postaci bitmapy.') 
message = input('> ')

if message == '':
    sys.exit()

for line in bitmap.splitlines():
    for i, bit in enumerate(line):
        if bit == ' ':
            print(' ', end='')
        else:
            print(message[i % len(message)], end ='')
    print()

