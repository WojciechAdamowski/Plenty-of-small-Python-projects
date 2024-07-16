"""
Generator kalendarza, autor: Al Sweigart, al@inventwithpython.com
Tworzy kartkę z kalendarza na dany miesiąc, zapisuje w pliku tekstowym i przygotowuje do druku.
Etykiety: krótki
"""

import datetime

DAYS = ('Niedziela', 'Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota')
MONTHS = ('Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec', 'Lipiec', 'Sierpień', 'Wrzesień', 'Październik', 'Listopad', 'Grudzień') 

print('Generator kalendarza') 

while True:
    print('Podaj rok dla kalendarza:')
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print('Podaj rok jako wartość liczbową, na przykład 2023.')

while True:
    print('Podaj miesiąc dla kalendarza, 1-12:')
    response = input('> ')
    if not response.isdecimal():
        print('Podaj miesiąc jako liczbę, na przykład 3 dla marca.')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break
    print('Podaj liczbę od 1 do 12.') 

def getCalendarFor(year, month):
    calText = ''
    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'
    calText += '.Niedziela.Poniedziałek..Wtorek.....Środa.....Czwartek....Piątek...Sobota..\n'

    weekSeparator = ('+----------' * 7) + '+\n'
    blankRow = ('|          ' * 7) + '|\n' 

    currentDate = datetime.date(year, month, 1)

    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=-1)

    while True:
        calText += weekSeparator

        dayNumberRow = ''

        for i in range (7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1)
        dayNumberRow += '|\n'

        calText += dayNumberRow

        for i in range(3):
            calText += blankRow

        if currentDate.month != month:
            break

    calText += weekSeparator
    return calText

calText = getCalendarFor(year, month)
print(calText) 

# Zapisz kalendarz w pliku tekstowym:
calendarFilename = 'kalendarz_{}_{}.txt'.format(year, month)

with open(calendarFilename, 'w') as fileObj:
    fileObj.write(calText)

print('Zapisano z nazwą ' + calendarFilename) 

