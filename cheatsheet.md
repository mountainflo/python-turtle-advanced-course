# Cheatsheet für Turtle Graphics und Python

Vollständige und ausführliche Turtle-Dokumentation:
[https://docs.python.org/3/library/turtle.html](https://docs.python.org/3/library/turtle.html)

Ausführliche deutsche Dokumentation für Python:
[https://py-tutorial-de.readthedocs.io/de/python-3.3/](https://py-tutorial-de.readthedocs.io/de/python-3.3/)

Für Turtle Graphics musst du auf repl.it ein neues repl erstellen. 
Als Sprache muss dafür "Python (with Turtle)" ausgewählt werden.


**[Turtle Graphics](#turtle-graphics)**

* [Neue Turtle erstellen](#neue-turtle-erstellen)
* [Basisbewegungen](#basisbewegungen)
* [Geschwindigkeit ändern](#geschwindigkeit-ändern)
* [Stift verändern](#stift-verändern)
* [Texte schreiben](#texte-schreiben)
* [Position abfragen und verändern](#position-abfragen-und-verändern)
* [Schildkörte ausblenden](#schildkröte-ausblenden)
* [Screen einrichten](#screen-einrichten)
* [Screen geöffnet halten](#screen-geöffnet-halten)
* [Steuerung per Tastatur](#steuerung-per-tastatur)

**[Python](#python)**

* [Variablen](#variablen)
* [Schleifen](#schleifen)
    * [for-Schleife](#for-schleife)
    * [while-Schleife](#while-schleife)
* [Listen](#listen)
* [Funktionen](#funktionen)
    * [Funktion ohne Parameter](#funktion-ohne-parameter)
    * [Funktion mit Parameter](#funktion-mit-parameter)
    * [Funktion mit Rückgabewert](#funktion-mit-rückgabewert)
* [Bedingungen (if-Abfragen)](#bedingungen-if-abfragen)
* [Operatoren](#operatoren)
    * [Vergleichsoperatoren](#vergleichsoperatoren)
    * [Logische Operatoren](#logische-operatoren)

**[Weitere hilfreiche Python-Module](#weitere-hilfreiche-python-module)**

* [random (Zufallszahlen)](#random-zufallszahlen)
* [time (Zeitbezogene Funktionen)](#time-zeitbezogene-funktionen)



## Turtle Graphics

### Neue Turtle erstellen

```python
import turtle
tina = turtle.Turtle()

tina.color("blue") # black, red, green, yellow, pink ...
tina.shape("turtle") # "arrow", "turtle", "circle", "square", "classic"
```

### Basisbewegungen

```python
tina.forward(100)
tina.backward(100)
tina.left(90) # Angabe in Grad
tina.right(90) # Angabe in Grad
tina.goto(0,0) # goto(x,y)
```

### Geschwindigkeit ändern

```python
tina.speed("normal") # "fastest", "fast", "normal", "slow", "slowest"
```

### Stift verändern

```python
tina.penup() # Stift anheben
tina.pendown() # Stift senken
tina.pensize(10) # Dicke des Stifts. Standard=1
```

### Texte schreiben

```python
tina.write("text",align="center") # align kann “left”, “center” oder right” sein
```

### Position abfragen und verändern

```python
tina.pos() # gibt Vektor mit (x, y) zurück
tina.xcor() # gibt x Koordinate zurück
tina.ycor() # gibt y Koordinate zurück
tina.setposition(0, 0) # x, y Position festlegen
```

### Schildkröte ausblenden

```python
tina.hideturtle()
```

### Screen einrichten

```python
window = turtle.Screen()

window.setup(width=400, height=400) # Bildschirmgröße festlegen
window.tracer(0)  # Bildschirm wird nur noch manuell aktualisiert
window.bgcolor("#B2FF66")  # Hintergrundfarbe
window.update()  # Bildschirm aktualisieren
```

### Screen geöffnet halten

```python
window = turtle.Screen()

# Programm wird nicht beendet, falls dies die letzte Codezeile ist
window.mainloop() 
```

### Steuerung per Tastatur

Die Codes für die Pfeiltasten sind: ```Up```, ```Down```, ```Left``` und ```Right```.

```python
window = turtle.Screen()

# Funktion wird ausgeführt, sobald die Taste gedrückt wird
window.onkey(functionName, "Up")
window.listen() # Ab sofort reagiert das Programm auf Tastatureingaben
```

## Python

### Variablen

```python
square_color = "blue" # Texte stehen in Anführungszeichen
square_size = 10 # Zahlen stehen nicht in Anführungszeichen
```

#### Globale Variablen in Funktionen verändern

```python
foo = 0

def foo_function():
    global foo
    foo = foo + 1
```

### Schleifen

#### for-Schleife

```python
for count in range(4): # Schleife wird 4 mal ausgeführt
    tina.forward(50)
    tina.left(90)
```

#### while-Schleife

```python
counter = 0
while counter < 4: # Schleife wird 4 mal ausgeführt
    tina.forward(50)
    tina.left(90)
    counter = counter + 1  
```

### Listen

```python
colors = ['red', 'purple', 'blue', 'green']

# durch alle Element der Liste iterieren
for color_name in colors:
    tina.color(color_name) 
    tina.forward(100) 
    tina.left(90)

colors.insert(1, 'yellow') # Neues Element an Index 1 einfügen
# => 'red', 'yellow', 'purple', 'blue', 'green'

del colors[0] # erstes Element ('red') löschen

colors[-1] # auf letztes Element in der Liste zugreifen

# Alle Elemente der Liste vom zweiten bis zum letzten ausgeben
for color_name in colors[1:]:
    print(color_name)
```

### Funktionen

#### Funktion ohne Parameter

```python
# Die Funktion zeichnet Quadrate mit der Seitenlänge 50
def square():
    for count in range(4):
        tina.forward(50)
        tina.left(90)

square() # Aufruf der Funktion
```

#### Funktion mit Parameter

```python
# Funktion, die Quadrate unterschiedlicher Seitenlänge zeichnet
# Es wird der Parameter "size" verwendet
def square(size):
    for count in range(4):
        tina.forward(size)
        tina.left(90)

square(100) # Aufruf der Funktion
```

#### Funktion mit Rückgabewert

```python
# Funktion mit Rückgabewert
def add_two_numbers(a, b):
    result = a + b
    return result

add_two_numbers(100, 42) # Aufruf der Funktion
```

### Bedingungen (if-Abfragen)

```python
a = 5
b = 9

if a > b :
    print("a ist größer als b") # wird nicht ausgeführt
elif a < b :
    print("a ist kleiner als b") # wird ausgeführt, da 5 < 9
else:
    print("a und b sind genau gleich groß")
```

### Operatoren

| Operator          | Bezeichnung |
| ------------- | ----- |
| ```+```, ```-``` | Addition, Subtraktion |
| ```*```, ```/```, ```%``` | Multiplikation, Subtraktion, Modulo (Rest) |

#### Vergleichsoperatoren

| Operator          | Bezeichnung |
| ------------- | ----- |
| ```<```, ```<=```  | "Kleiner" und "Kleiner Gleich" |
| ```>```, ```>=``` | "Größer" und "Größer Gleich" |
| ```==``` | Gleichheit |
| ```!=``` | Ungleichheit |

#### Logische Operatoren

| Operator          | Bezeichnung |
| ------------- | ----- |
| ```and``` | Logisches "Und". Gibt ```True``` zurück, wenn *beide* Anweisungen ```True``` sind. |
| ```or```  | Logisches "Oder". Gibt ```True``` zurück, wenn *eine der beiden* Anweisungen ```True``` ist.|

## Weitere hilfreiche Python-Module

### random (Zufallszahlen)

```python
from random import randint

untere_grenze = 5
obere_grenze = 10

randint(untere_grenze, obere_grenze)
```

### time (Zeitbezogene Funktionen)

```python
import time

# Ausführung des Programms stoppt für X Sekunden
time.sleep(0.5) # Ausführung stoppt für 0,5 Sekunden
``` 
