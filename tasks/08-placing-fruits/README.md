## 8. Früchte zufällig auf dem Spielfeld platzieren

Das Spiel wird nun etwas interessanter. Wir platzieren jetzt eine Frucht auf dem Spielfeld. Sobald die Schlange
die Frucht erreicht hat, wird eine Frucht erstellt. Die neue Frucht wird irgendwo zufällig auf dem Spielfeld platziert.

### 8.1 Neue rote Frucht erstellen

Als erstes erstellst du eine neue Frucht. Füge dazu den nachfolgenden Code unterhalb der Stelle ein,
wo du die Schlange erstellt hast.

```python
fruit = turtle.Turtle()
fruit.color("red")
fruit.shape("square")
fruit.penup()
```

### 8.2 Kollision mit Turtle überprüfen

Wir schreiben nun eine Funktion, die überprüft, ob ein Turtle-Objekt (Schlange oder Frucht),
mit gegebenen x- und y-Koordinaten kollidiert. Erstelle dazu eine neue Funktion mit dem Namen
```check_for_collision_with_turtle_obj(x, y, turtle_obj)```.

In der Funktion gibst du ```True``` zurück, falls ```turtle_obj.xcor() == x``` und
```turtle_obj.ycor() == y``` ist. Die zwei Bedingungen kannst du in der ```if```-Abfrage mit ```and```
verknüpfen. Ansonsten verlässt du die Funktion mit dem Rückgabewert ```False```.

**Anmerkung:** ```and``` ist ein logischer Operator, mit dem zwei Bedingungen verknüpft werden können. 
Nur wenn beide Bedingungen ```True``` sind, ist auch das Gesamtergebnis ```True```.

### 8.3 Zufällige Position für Früchte generieren

Die Platzierung von Früchten übernimmt wieder eine neue Funktion, die wir ```place_fruit()``` nennen.
In einer ```while```-Schleife wird in der neuen Funktion solange eine zufällige Position generiert,
bis wir eine Position haben, die noch nicht von der Schlange besetzt ist.

Die zufälligen x-/y-Koordinaten generierst du mit den nachfolgenden Codezeilen. Achte darauf, dass du die
```import```-Anweisung ganz oben in dein Programm einfügst. Die anderen zwei Zeilen kopierst du in die
```while```-Schleife in der ```place_fruit()```-Funktion.

```python
from random import randint

x = randint(-9, 9) * 20
y = randint(-9, 9) * 20
```

Wir überprüfen in der ```while```-Schleife jetzt noch, ob die Position der Frucht auch nicht der Position
der Schlange entspricht. Wir möchten vermeiden, dass die Frucht und die Schlange genau auf dem selben Feld sind.
Die Funktion ```check_for_collision_with_turtle_obj(x, y, snake_head)```, aus der vorherigen Teilaufgabe
nimmt uns dazu bereits den größten Teil der Arbeit ab. Mit einer ```if```-Anweisung musst du nur den Rückgabewert
der Funktion ```check_for_collision_with_turtle_obj()``` überprüfen. Gibt die Funktion ```False``` zurück,
kannst du die Frucht auf die neue Position setzen und anschließend die ```while```-Schleife verlassen.
Falls die Funktion ```True``` zurückgibt, musst die Schleife nochmal druchlaufen werden und nochmal neue zufällige
x-/y-Koordinaten generiert werden.

*Erweiterung: Wenn du möchtest, kannst du die Funktion so umschreiben, dass sie Früchte auf jeder beliebigen
Spielfeldgröße platzieren kann. Evtl. benötigst du dazu noch den Python-Befehl ```int()```, mit dem du
Kommazahlen in ganze Zahlen umwandeln kannst.*

### 8.4 Neue Frucht erstellen, sobald die Schlange die Position der Frucht erreicht

Jedes mal, wenn sich die Schlange um ein Feld bewegt, müssen wir überprüfen, ob die Schlange nun
eine Frucht getroffen hat. Du kannst dazu in der ```move()```-Funktion die Funktion
```check_for_collision_with_turtle_obj(x, y, fruit)``` verwenden. Erst wenn ```check_for_collision_with_turtle_obj```
```True``` zurück gibt, muss eine neue Frucht erstellt werden. D.h. dann musst du die Funktion
```place_fruit()``` aufrufen.