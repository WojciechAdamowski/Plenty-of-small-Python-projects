# Plenty-of-small-Python-projects
A repository created for learning Python, based on the book "The Big Book of Small Python Projects" by Al Sweigart

## Prepare project 

1. Check that Python is installed
```
py --version
```

2. Create Python virtual environment
```
python -m venv venv
```

3. Activate Python virtual environment
```
.\venv\Scripts\Activate.ps1
```

4. Install all libraries
```
pip install -r requirements.txt
```

5. Deactivate virtual environment
```
deactivate
```

* If there is any problems with playsound use following code in activated virtual environment:
```
pip install --upgrade setuptools wheel
pip install playsound
pip install -r requirements.txt
```

## Projects 
1. Bagles
    - input('String')
    - 'String'.format()
    - 'String'.lower()
    - 'String'.startswith('String')
    - list('String')
    - list.sort()
    - random.shuffle(list)

    ```
    .\venv\Scripts\Activate.ps1
    python ".\1. Bagels\Bagels.py"
    deactivate
    ```

2. Birthday paradox
    - random.randint(int, int)
    - datetime.timedelta(int)
    - datetime.date(int_year, int_month, int_day)
    - enumerate(list)
    - round(int, int)
    - 100_000

    ```
    .\venv\Scripts\Activate.ps1
    python ".\2. Birthday paradox\BirthdayParadox.py"
    deactivate
    ```

3. Bitmap
    - open('String_file_name', 'String_open_type')
    - file.read()
    - 'String'.splitlines()
    - sys.exit()

    ```
    .\venv\Scripts\Activate.ps1
    python ".\3. Bitmap\Bitmap.py"
    deactivate
    ```

4. Blackjack
    - 'String'.ljust(int)
    - 'String'.rjust(int)
    - chr(int) 

    ```
    .\venv\Scripts\Activate.ps1
    python ".\4. Blackjack\Blackjack.py"
    deactivate
    ```

5. DVD
    - random.choice(list)
    - random.randint(int, int)

    ```
    .\venv\Scripts\Activate.ps1
    python ".\5. DVD\DVD.py"
    deactivate
    ```

6. Caesar cipher
    - list.find(list_element)

    ```
    .\venv\Scripts\Activate.ps1
    python ".\6. Caesar Cipher\CaesarCipher.py"
    deactivate
    ```

7. Caesar hacker

    ```
    .\venv\Scripts\Activate.ps1
    python ".\7. Caesar Hacker\CaesarHacker.py"
    deactivate
    ```

8. Calendar maker
    - date.weekday() 
    - 'String'.isdecimal()
    - conditional <= conditional <= conditional 
    
    ```
    .\venv\Scripts\Activate.ps1
    python ".\8. Calendar maker\CalendarMaker.py"
    deactivate
    ```
    ```

9. Carrot in box
    - 'Strirng'.center(int)
    
    ```
    .\venv\Scripts\Activate.ps1
    python ".\9. Carrot in box\CarrotInBox.py"
    deactivate
    ```

10. Cho-han
    - int // 10 
    
    ```
    .\venv\Scripts\Activate.ps1
    python ".\10. Cho-han\ChoHan.py"
    deactivate
    ```
    
11. Click bait
    
    ```
    .\venv\Scripts\Activate.ps1
    python ".\11. Click bait\ClickBait.py"
    deactivate
    ```
    
12. Collatz
    - print('String', end='', flush=True)
    
    ```
    .\venv\Scripts\Activate.ps1
    python ".\12. Collatz\Collatz.py"
    deactivate
    ```

13. Conways game of life
    - copy.deepcopy(dictionary)
    
    ```
    .\venv\Scripts\Activate.ps1
    python ".\13. Conways game of life\ConwaysGameOfLife.py"
    deactivate
    ```

14. Count down
    - copy.deepcopy(dictionary)
    
    ```
    .\venv\Scripts\Activate.ps1
    python ".\14. Count down\CountDown.py"
    deactivate
    ```

15. Deep cave
    - 
    
    ```
    .\venv\Scripts\Activate.ps1
    python ".\15. Deep cave\DeepCave.py"
    deactivate
    ```






