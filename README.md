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
