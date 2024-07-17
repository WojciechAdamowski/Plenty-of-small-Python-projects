"""
Gra w życie Conwaya
Klasyczna symulacja automatu komórkowego. Naciśnij Ctrl+C, by zatrzymać program.
Etykiety: krótki, artystyczny, symulacja
"""

import copy, random, sys, time

WIDTH = 79 
HEIGHT = 20

ALIVE = 'o'
DEAD = ' '

nextCells = {}

for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = ALIVE
        else:
            nextCells[(x, y)] = DEAD

while True:
    print(nextCells)
    print('\n' * 50)

    cells = copy.deepcopy(nextCells) 

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x, y)], end='') # Wyświetl # lub spację.
        print() # Wyświetl znak nowej linii na końcu wiersza.
    print('Naciśnij Ctrl+C, by wyjść.')

     # Oblicz następny krok na podstawie aktualnego stanu komórek:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Pobranie współrzędnych (x, y) sąsiednich komórek, nawet jeśli
            # zawijają się na drugą krawędź:
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT
    
            # Policz żywych sąsiadów:
            numNeighbors = 0

            if cells[(left, above)] == ALIVE:
                numNeighbors += 1 # Górny lewy sąsiad jest żywy.
            if cells[(x, above)] == ALIVE:
                numNeighbors += 1 # Górny sąsiad jest żywy.
            if cells[(right, above)] == ALIVE:
                numNeighbors += 1 # Górny prawy sąsiad jest żywy.
            if cells[(left, y)] == ALIVE:
                numNeighbors += 1 # Lewy sąsiad jest żywy.
            if cells[(right, y)] == ALIVE:
                numNeighbors += 1 # Prawy sąsiad jest żywy.
            if cells[(left, below)] == ALIVE:
                numNeighbors += 1 # Dolny lewy sąsiad jest żywy.
            if cells[(x, below)] == ALIVE:
                numNeighbors += 1 # Dolny sąsiad jest żywy
            if cells[(right, below)] == ALIVE:
                numNeighbors += 1 # Dolny prawy sąsiad jest żywy.

                # Ustaw stan komórki według zasad gry w życie Conwaya:
            if cells[(x, y)] == ALIVE and (numNeighbors == 2 or numNeighbors == 3):
                # Żywe komórki z dwoma lub trzema sąsiadami pozostają żywe:
                nextCells[(x, y)] = ALIVE
            elif cells[(x, y)] == DEAD and numNeighbors == 3:
                # Martwe komórki z dokładnie trzema sąsiadami ożywają:
                nextCells[(x, y)] = ALIVE
            else:
                # Pozostałe komórki umierają lub pozostają martwe:
                nextCells[(x, y)] = DEAD 

    try:
        time.sleep(1) # Dodaj 1-sekundową pauzę, by zmniejszyć efekt migania.
    except KeyboardInterrupt:
        print("Gra w życie Conwaya")
        sys.exit() # Po naciśnięciu Ctrl+C zakończ program. 