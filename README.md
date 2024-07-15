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

    ```
    .\venv\Scripts\Activate.ps1
    python ".\4. Blackjack\Blackjack.py"
    deactivate
    ```






