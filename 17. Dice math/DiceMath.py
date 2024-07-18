"""
Matematyka i kostki
Program, który sprawdza jak szybko potrafisz dodawać wyrzucone na kostkach oczka.
Etykiety: długi, artystyczny, gra, matematyka
"""

import random, time 

DICE_WIDTH = 9
DICE_HEIGHT = 5
CANVAS_WIDTH = 79
CANVAS_HEIGHT = 24 - 3

QUIZ_DURATION = 30
MIN_DICE = 2
MAX_DICE = 6

REWARD = 4
PENALTY = 6

assert MAX_DICE < 14

D1 = (['+-------+',
       '|       |',
       '|   O   |',
       '|       |',
       '+-------+'], 1)

D2a = (['+-------+',
        '| O     |',
        '|       |',
        '|     O |',
        '+-------+'], 2)

D2b = (['+-------+',
        '|     O |',
        '|       |',
        '| O     |',
        '+-------+'], 2)

D3a = (['+-------+',
        '| O     |',
        '|   O   |',
        '|     O |',
        '+-------+'], 3)

D3b = (['+-------+',
        '|     O |',
        '|   O   |',
        '| O     |',
        '+-------+'], 3)

D4 = (['+-------+',
       '| O   O |',
       '|       |',
       '| O   O |',
       '+-------+'], 4)

D5 = (['+-------+',
       '| O   O |',
       '|   O   |',
       '| O   O |',
       '+-------+'], 5)

D6a = (['+-------+',
        '| O   O |',
        '| O   O |',
        '| O   O |',
        '+-------+'], 6)

D6b = (['+-------+',
        '| O O O |',
        '|       |',
        '| O O O |',
        '+-------+'], 6)

ALL_DICE = [D1, D2a, D2b, D3a, D3b, D4, D5, D6a, D6b]

print('''
Matematyka i kości

Dodaj oczka wszystkich kości na ekranie. Masz {} sekund,
by podać jak największą liczbę odpowiedzi. Otrzymujesz {} punkty za każdą
poprawną odpowiedź i tracisz {} punkt za każdą złą odpowiedź.
'''.format(QUIZ_DURATION, REWARD, PENALTY))

input('Naciśnij Enter, aby rozpocząć...')

correctAnswers = 0
incorrectAnswers = 0
startTime = time.time()

while time.time() < startTime + QUIZ_DURATION:
    sumAnswer = 0 
    diceFaces = []

    for i in range(random.randint(MIN_DICE, MAX_DICE)):
        die = random.choice(ALL_DICE)
        diceFaces.append(die[0])
        sumAnswer += die[1]

    topLeftDiceCorners = []

    for i in range(len(diceFaces)):
        while True:
            left = random.randint(0, CANVAS_WIDTH - 1 - DICE_WIDTH)
            top = random.randint(0, CANVAS_HEIGHT - 1 - DICE_HEIGHT)

            topLeftX = left
            topLeftY = top
            topRightX = left + DICE_WIDTH
            topRightY = top
            bottomLeftX = left
            bottomLeftY = top + DICE_HEIGHT
            bottomRightX = left + DICE_WIDTH
            bottomRightY = top + DICE_HEIGHT

            overlaps = False

            for prevDieLeft, prevDieTop in topLeftDiceCorners:
                prevDieRight = prevDieLeft + DICE_WIDTH
                prevDieBottom = prevDieTop + DICE_HEIGHT

                for cornerX, cornerY in ((topLeftX, topLeftY),
                                         (topRightX, topRightY),
                                         (bottomLeftX, bottomLeftY),
                                         (bottomRightX, bottomRightY)):
                    if (prevDieLeft <= cornerX < prevDieRight
                        and prevDieTop <= cornerY < prevDieBottom):
                            overlaps = True
            if not overlaps:
                # Kości nie zachodzą na siebie, więc możemy wyświetlić kostkę w tym miejscu:
                topLeftDiceCorners.append((left, top))
                break

    canvas = {}

    for i, (dieLeft, dieTop) in enumerate(topLeftDiceCorners):
        dieFace = diceFaces[i]
        for dx in range(DICE_WIDTH):
            for dy in range(DICE_HEIGHT):
                canvasX = dieLeft + dx
                canvasY = dieTop + dy
                canvas[(canvasX, canvasY)] = dieFace[dy][dx]

    for cy in range(CANVAS_HEIGHT):
        for cx in range(CANVAS_WIDTH):
            print(canvas.get((cx, cy), ' '), end='')
        print()

    response = input('Podaj sumę: ').strip()
    if response.isdecimal() and int(response) == sumAnswer:
        correctAnswers += 1
    else:
        print('Źle, poprawna odpowiedź to ', sumAnswer)
        time.sleep(2)
        incorrectAnswers += 1

score = (correctAnswers * REWARD) - (incorrectAnswers * PENALTY)
print('Poprawne odpowiedzi:  ', correctAnswers)
print('Niepoprawne odpowiedzi:', incorrectAnswers)
print('Wynik:    ', score)
                    

