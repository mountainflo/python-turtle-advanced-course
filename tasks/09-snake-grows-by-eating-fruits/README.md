## 9. Schlange wächst, sobald sie eine Frucht isst

Bisher passiert unsere Schlange eine Frucht und eine neue Frucht wird darauf an einer anderen freien Position
auf dem Spielfeld platziert. Wenn die Schlange die Frucht erreicht, wächst sie bisher aber noch nicht.
In dieser Aufgabe werden wir die Schlange um eine Element wachsen lassen, sobald der Kopf der Schlange auf ein
Feld mit einer Frucht gelangt.

### 9.1 Liste mit den Elementen der Schlange erstellen

Neben dem Kopf der Schlange ```snake_head``` und der Frucht ```fruit``` erstellen wir nun eine Liste, die alle
Elemente der Schlange beinhaltet. Die Liste enthält am Anfang nur den Kopf der Schlange. Jedes mal, wenn der
Schlangenkopf ein Feld mit einer Frucht erreicht, wächst die Liste um ein Element, bzw. die Schlange wird
ein Element länger.

Die Liste erstellst du kannst am Anfang des Programms unterhalb der Definitionen zum ```snake_head```.
Mit ```snake = [snake_head]``` erstellst du eine Liste, die bereits als erstes Element den Kopf der Schlange enthält.

### 9.2 Schlange um ein Element erweitern

In der Aufgabe 8.4 haben wir jedes mal, wenn die Schlange über ein Feld mit einer Frucht läuft, eine neue Frucht erstellt.
Vor dem Aufruf der Funktion ```place_fruit()```, müssen wir nun die Schlange um ein Element verlängern.

Bevor wir dies tun, müssen wir die Position des Schlangenkopfs, bevor dieser um ein Feld verschoben wird, zwischenspeichern.
Erweitere dazu die ersten Zeilen der ```move()```-Funktion, wie folgt:

```python
x = snake_head.xcor()
y = snake_head.ycor()
x_old = x
y_old = y
```

Gehe nun zurück an die Anstelle, bevor der Aufruf der Funktion ```place_fruit()``` erfolgt.
Hier erstellst du ein neues Schlangen-Element mit ```snake_body_elem = turtle.Turtle()```. Achte darauf,
dem Schlangen-Element, die gleiche Farbe und Form, wie dem Schlangenkopf zu geben.
Nachdem Erstellen des neuen Schlangen-Elements, setzt du es auf die Position, auf der zuvor noch der Kopf war.
Die Koordinaten dazu haben wir in ```x_old``` und ```y_old``` gespeichert.

Anschließend musst du das neue Schlangen-Element noch zur Liste hinzufügen. Füge das neue Element bei Index 1,
direkt nach dem Schlangenkopf ein. Dies kannst du mit ```snake.insert(1, snake_body_elem)``` machen.

### 9.3 Schlange trifft keine Frucht und muss verschoben werden

Falls die Schlange keine Frucht trifft, läuft sie einfach ganz normal weiter. Wir verschieben dazu nicht
jedes Element der Schlange um ein Feld nach vorne, sondern nehmen nur das letzte Feld und platzieren es
auf die Stelle (```x_old``` und ```y_old```), wo zuvor noch der Kopf war.
 
In der Liste ```snake```, verschieben wir das letzte Element noch an die zweite Stelle der Liste. Das Element
steht danach direkt nach dem Schlangenkopf in der Liste.

Wie du auf das letzte Element der Liste zugreifen und wie du ein Element in der Liste löschen kannst,
steht im Cheatsheet unter dem Punkt "Listen". Wie du ein Element an einer bestimmten Position in der Liste
einfügen kannst, hast du bereits in der Teilaufgabe 9.2 gesehen.

### 9.4 Liste mit den Schlangen-Elementen beim Neustart zurücksetzen

Mit der Taste "p" kannst du das Spiel neu starten, falls du einmal verloren hast. Beim Neustart enthält
die Schlange aber immer noch alle Elemente aus dem letzten Durchlauf.
Du musst deshalb in der Funktion ```initialize_board()``` noch alle Elemente, bis auf den Kopf aus
der Liste entfernen. Verwende dazu die nachfolgende ```for```-Schleife:

```python
for elem in snake[1:]:
    elem.hideturtle()
    del elem
```

Die Schleife startet nach dem ersten Element in der Liste (```snake[1:]```) und läuft bis zum Ende der Liste.
Der Schlangenkopf bleibt somit erhalten.