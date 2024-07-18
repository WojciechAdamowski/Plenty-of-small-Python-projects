r"""Diamenty
Program rysuje różnej wielkości diamenty.
                           /\       /\
                          /  \     //\\
            /\     /\    /    \   ///\\\
           /  \   //\\  /      \ ////\\\\
 /\   /\  /    \ ///\\\ \      / \\\\////
/  \ //\\ \    / \\\///  \    /   \\\///
\  / \\//  \  /   \\//    \  /     \\//
 \/   \/    \/     \/      \/       \/
Etykiety: króciutki, dla początkujących, artystyczny"""

def main():
    print('Diamenty')

    # Wyświetl diamenty o wielkości od 0 do 6:
    for diamondSize in range(6):
        displayOutlineDiamond(diamondSize)
        print()  # Wyświetl znak nowej linii.
        displayFilledDiamond(diamondSize)
        print()  # Wyświetl znak nowej linii.


def displayOutlineDiamond(size):
    print('Size: {}\n'.format(size))
    # Wyświetl górną połówkę diamentu:
    for i in range(size):
        print(' ' * (size - i - 1), end='')  # Odstęp z lewej strony.
        print('/', end='')  # Lewa strona diamentu.
        print(' ' * (i * 2), end='')  # Środek diamentu.
        print('\\')  # Prawa strona diamentu.

    # Wyświetl dolną połówkę diamentu:
    for i in range(size):
        print(' ' * i, end='')  # Odstęp z lewej strony.
        print('\\', end='')  # Lewa strona diamentu.
        print(' ' * ((size - i - 1) * 2), end='')  # Środek diamentu.
        print('/')  # Prawa strona diamentu.


def displayFilledDiamond(size):
    # Wyświetl górną połówkę diamentu:
    for i in range(size):
        print(' ' * (size - i - 1), end='')  # Odstęp z lewej strony.
        print('/' * (i + 1), end='')  # Lewa strona diamentu.
        print('\\' * (i + 1))  # Prawa strona diamentu.

    # Wyświetl dolną połówkę diamentu:
    for i in range(size):
        print(' ' * i, end='')  # Odstęp z lewej strony.
        print('\\' * (size - i), end='')  # Lewa strona diamentu.
        print('/' * (size - i))  # Prawa strona diamentu.


# Jeśli program został uruchomiony (a nie zaimportowany), rozpocznij grę:
if __name__ == '__main__':
    main()