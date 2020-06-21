# Python Fortgeschrittenen Kurs

**Kursbeschreibung:**

Der Kurs setzt Grundkenntnisse in Python voraus. Mit Grundkenntnissen sind Variablen, 
Schleifen, Bedingungen und erste einfache Funktionen gemeint. Am Anfang gibt es zur Wiederholung
nochmals eine Einführung in Funktionen.

Während des Kurses wird das Spiel *Snake* programmiert. Dabei werden Kenntnisse und die Verwendung 
von Listen und Funktionen vertieft. Die Teilnehmer sollen sich auch mit dem Aufbau eines Spiels 
und dessen einzelner Bestandteile auseinandersetzen. Des weiteren sollen die Teilnehmer nach dem 
Kurs für eigene Programme, selbstständig Informationen aus Dokumentationen ziehen können.

**Voraussetzungen:**

Account auf [repl.it](http://www.repl.it)

**Dokumentation:**

Vollständige und ausführliche Turtle-Dokumentation:
[https://docs.python.org/3/library/turtle.html](https://docs.python.org/3/library/turtle.html)

Ausführliche deutsche Dokumentation für Python:
[https://py-tutorial-de.readthedocs.io/de/python-3.3/](https://py-tutorial-de.readthedocs.io/de/python-3.3/)

## 1. Das Spiel "Snake"

Die Teilnehmer (TNs) dürfen in 2er-Teams das Spiel Snake ([https://playsnake.org](https://playsnake.org)) 
ausprobieren. Jedes Team soll alle wichtigen Spielelemente und Regeln von "Snake" aufschreiben.

Nach der Phase in den einzelnen Teams werden die Spielelemente und Regeln von allen zusammengetragen. 
Hierbei sollten die TNs folgende Punkte erkennen:

* **Schlange:** Eine Schlange besteht aus ein oder mehreren Elementen und kann über die Pfeiltasten bewegt werden. Sobald sich die Schlange selbst beißt, ist das Spiel zu Ende.
* **Spielfeld:** Das Spielfeld ist begrenzt und darf nicht von der Schlange berührt werden, ansonsten ist das Spiel beendet. Das Spielfeld besteht aus einem Raster. Jedes Feld ist genauso groß, wie ein Schlangenelement.
* **Früchte:** Die Früchte können von der Schlange gegessen werden. Sobald sie auf das Feld der Frucht gelangt, wächst die Schlange um ein Element. Anschließend wird eine neue Frucht auf einem anderen zufällig gewählten Feld platziert.

## 2. Wiederholung Funktionen und kurze Einführung in Turtle

* Kurze Wiederholung zu Funktionen mit Rückgabewerten und Parametern. Erklären, warum Funktionen sinnvoll sind.
Funktionen sollten von den Teilnehmern verstanden werden, da diese intensiv im weiteren Kurs verwendet werden.
Ohne ein Grundverständis über Funktionen könnten die weiteren Kursinhalte zu schwierig sein.
* Kurz erklären, was Turtle ist und wie es funktioniert.

Bei Unklarheiten können die Teilnehmer jederzeit Fragen stellen oder im Cheatsheet nachschauen.
Im Cheatsheet sind alle notwendigen Python- und Turtle-Befehle aufgeführt.

## 3. Keyboard-Bindings kennen lernen

Die Schlange soll über die Pfeiltasten auf der Tastatur bewegt werden. Zuerst wollen wir die sogannten
Keyboard-Bindings kennen lernen. Damit lässt sich an eine Taste auf der Tastatur eine Funktionen binden.
Sobald die Taste gedrückt wird, wird die Funktion ausgeführt.

Ihr sollt nun zwei Funktionen schreiben ```go_right()``` und ```go_left()```, mit denen die Schlange nach rechts
und links über das Spielfeld bewegt werden kann. Mit dem Befehl ```window.onkey()``` könnt ihr eine Funktion
an eine bestimmte Taste binden. Für die Pfeiltaste nach rechts müsst ihr z.B. ```window.onkey(go_right, "Right")```
schreiben. Sobald die Taste ```"Right"``` gedrückt wird, wird damit die Funktion ```go_right()``` ausgeführt.

In den Funktionen ```go_right()``` und ```go_left()``` sollt ihr zuerst die aktuelle x-Position
der Schlange abfragen. Anschließend verschiebt ihr die Schlange um **20 Einheiten** nach rechts, bzw.
nach links. Mit ```xcor()``` bekommt ihr die aktuelle x-Position der Schlange und mit ```setx()``` könnt
ihr die x-Position der Schlange verändern.

Verwendet für diese Aufgabe die Datei [03-turtle-keyboard-binding-template.py](tasks/03-keyboard-bindings/03-turtle-keyboard-binding-template.py).
Ersetzt in dieser Datei die ```TODO```-Kommentare mit den richtigen Python-Befehlen.

*Weitere Details, wie die Steuerung über die Tastatur oder das Abfragen und Verändern der Position funktioniert,
findet ihr im Cheatsheet unter: "Position abfragen und verändern" und "Steuerung per Tastatur".*

## 4. Schlange bewegt sich selbstständig vorwärts

In dieser Aufgabe soll sich die Schlange automatisch alle 0.2 Sekunden nach links oder rechts bewegen.
Die Taste, die als letztes gedrückt wurde, gibt die Richtung an, in die sich die Schlange bewegt.

Wird zum Beispiel die rechte Pfeiltaste gedrückt, läuft die Schlange nach rechts. 
Die Schlange läuft nun solange nach rechts weiter, bis die linke Pfeiltaste gedrückt wird.

### 4.1 Bildschirm manuell aktualisieren

Bisher hat sich der Bildschirm nach jeder Bewegung der Schlange sofort selbst aktualisiert.
Sobald wir die Position verändert haben, wurde die Schlange auf dem Bildschirm auf die neue Position gesetzt.
Wir möchten nun den Bildschirm mit der Schlange manuell aktualisieren.

Mit ```window.tracer(0)``` können wir die sofortige automatische Aktualisierung des Bildschrims
deaktivieren. Füge ```window.tracer(0)``` unterhalb des Befehls ```window.bgcolor("#B2FF66")``` ein.

Probiere aus, was passiert, wenn du jetzt das Programm startest. Die Schlange bewegt sich jetzt nicht mehr.
Damit sich die Schlange wieder bewegt, müssen wir die Darstellung auf dem Bildschirm manuell aktualisieren.
Füge dazu jedes mal, nachdem du den x-Wert neu gesetzt hast ```window.update()``` ein.

### 4.2 Schlange über globale Variable für die Richtung steuern 

In den beiden Funktionen ```go_right()``` und ```go_left()``` bewegen wir jetzt nicht mehr direkt die Schlange,
sondern verändern die globale Variable ```snake_head_direction```. ```snake_head_direction``` speichert
die Richtung der zuletzt gedrückten Pfeiltaste.
Füge dazu den nachfolgenden Code ganz oben, unterhalb von ```import turtle``` ein.

```python
# head directions
HEAD_DIRECTION_LEFT = 0
HEAD_DIRECTION_RIGHT = 1

snake_start_direction = HEAD_DIRECTION_RIGHT  # rechts ist die Richtung, in die gestartet wird
snake_head_direction = snake_start_direction
```

Lösche nun alles aus den beiden Funktionen ```go_right()``` und ```go_left()``` und ändere darin nur die
Variable ```snake_head_direction```. Setze die Variable auf ```HEAD_DIRECTION_LEFT```, wenn die linke
Pfeiltaste gedrückt wird und auf ```HEAD_DIRECTION_RIGHT```, wenn die rechte Pfeiltaste gedrückt wird.

*HINWEIS: Schaue im Cheatsheet unter "Globale Variablen in Funktionen verändern" nach, wie du den Wert
der globalen Variable ```snake_head_direction``` verändern kannst.*

### 4.3 Schleife erstellen und Schlange automatisch vorwärts bewegen

Damit sich die Schlange selbstständig, ohne eine Taste zu drücken bewegt, benötigen wir eine Schleife.
Während eines Schleifendurchlaufs, bewegen wir die Schlange um ein Feld nach rechts oder links.
Die Schlange wird in der Schleife immer in die Richtung der zuletzt gedrückten Pfeiltaste bewegt.
Nachdem die Schlange um ein Feld bewegt wurde, "schläft" das Programm für 0.2 Sekunden. 
Erst nach der kurzen Pause erfolgt der nächste Schleifendurchlauf.

1. Erstelle nun eine ```while True```-Schleife, die du oberhalb von ```window.mainloop()``` und nach ```window.listen()```
einfügst. 
2. In der Schleife speicherst du dir zuerst die zuletzt gedrückte Pfeiltaste in der lokalen Variable ```direction``` ab.
3. Wenn die lokale Variable ```direction``` der rechten Pfeiltaste entspricht, verschiebst du die Schlange um 20 nach rechts, ansonsten um 20 nach links.
4. Am Ende wird mit ```window.update()``` die Anzeige auf dem Bildschirm aktualisiert.
5. Vor dem nächsten Schleifendurchlauf soll das Programm 0.2 Sekunden pausieren.
Denn Befehl dazu findest du im Cheatsheet unter "time (Zeitbezogene Funktionen)".

### 4.4 Schlange bewegt sich in alle 4 Richtungen

Das Programm aus der vorherigen Aufgabe soll so erweitert werden, dass sich die Schlange nun in
alle 4 Richtungen (links, rechts, oben, unten) bewegt. Ergänze dazu noch die fehlenden
Funktionen ```go_up()``` und ```go_down()```, sowie die beiden fehlenden Variablen für die Richtungen
(```HEAD_DIRECTION_UP``` und ```HEAD_DIRECTION_DOWN```).

Für die beiden Funktionen ```go_up()``` und ```go_down()``` musst du auch noch die Keyboard-Bindings
für die Pfeiltasten ```"Up"``` und ```"Down"``` erstellen.

In der ```while```-Schleife müssen noch die Bewegungen nach oben und nach unten ergänzt weden,
falls die zuletzt gedrückte Pfeiltaste ```HEAD_DIRECTION_UP``` oder ```HEAD_DIRECTION_DOWN``` war.

Zur Vereinfachung der ```while```-Schleife und für mehr Übersichtlichkeit im Code, erstellst du eine
neue Funktion ```move()```. Die while-Schleife besteht anschließend nur noch aus:

```python
while True:
    move()
    window.update()
    time.sleep(0.2)
```

Die if-Abfragen, in welche Richtung die Schlange bewegt werden soll, werden alle in die Funktion
```move()``` ausgelagert.

## 5. Spielfeld-Rahmen zeichnen

*Anmerkung: Der Spielfeld-Rahmen ist nur wichtig, wenn das Spiel lokal verwendet wird. Für repl.it ist der Rahmen
nicht unbedingt notwendig. Aufgabe kann somit auch übersprungen werden.*

Schreibe eine Funktion ```draw_screen_border()```, die einen schwarzen Rahmen um das Spielfeld zeichnet.
In der Funktion erstellst du dazu eine neue Schildkröte mit ```pen = turtle.Turtle()```.
Blende die Schildkröte mit ```pen.hideturtle()``` aus, sodass diese beim Zeichnen nicht sichtbar ist.

Die Dicke des Rahmens kannst du z. B. über ```pen.pensize(4)``` auf 4 vergrößern.

Achte darauf, dass du beim Verschieben der Schildkröte vom Mittelpunkt des Spielfelds zum äußeren Rahmen
des Spielfelds noch keine Linie zeichnest. Mit ```pen.penup()``` und ```pen.pendown()``` kannst du den
"Stift" der Schildkröte anheben und senken. Somit kannst du die Schildkröte bewegen, auch ohne dabei eine
Linie zu zeichnen.

Den Aufruf der Funktion ```draw_screen_border()``` platzierst du noch vor den Keyboard-Bindings.

## 6. Spiel beenden, sobald die Schlange den Spielfeldrand berührt

Das Spiel soll nun so erweitert werden, dass beim Berühren des Spielfeldrands das Spiel beendet wird.
Die Schlange darf sich nur innerhalb des Spielfeldes bewegen.

Erstelle hierzu die Funktion ```check_for_collision_with_boundaries(x, y)```. Die Funktion erhält
die aktuelle x-Koordinate und y-Koordinate der Schlange. In der Funktion überprüfst du, ob sich die Koordinaten
**außerhalb des Spielfeldrands oder darauf** befinden.
Wenn die Schlange außerhalb des Spielfeldes ist, also mit dem Rahmen bereits kollidiert ist, 
beendest du die Funktion mit ```return True```. Wenn die Schlange noch innerhalb des Spielfeldes ist, gibst
du  ```False``` zurück.

**Wichtig:** Das Spielfeld ist zwar 400x400 groß, aber das Spielfeld befindet sich mittig auf einem Koordinatensystem.
Das heißt der linke Rand ist z.B. bei x=-200 und der rechte Rand ist bei x=+200.

Bevor du in der Funktion ```move()``` die neue x-/y-Position der Schlange setzt, rufst du die Funktion
```check_for_collision_with_boundaries(x, y)``` auf. Falls diese ```True``` liefert, beendest du sofort die
```move()```-Funktion mit ```return False```.
Wenn ```check_for_collision_with_boundaries(x, y)``` als Rückgabewert ```False``` liefert, kannst du wie zuvor,
die neue Position der Schlange setzen. Verlasse anschließend die Funktion mit ```return True```.

Wir verändern nun die ```while```-Schleife. Falls die Schlange den Spielfeldrand berührt, wird die Schleife
verlassen und das Spiel ist beendet. Der Rückgabewert von ```move()``` gibt uns Auskunft darüber, ob das Spiel
beendet ist oder ob es noch weiter laufen kann.

```python
play_game = True
while play_game:
    play_game = move()
    window.update()
    time.sleep(0.2)
```

## 7. Spiel per Tastendruck starten

Bisher startete das Spiel immer automatisch, sobald wir das Python-Programm gestartet haben.
Wir bauen das Spiel nun so um, so dass es erst beim Drücken der Taste "p" (p=play) gestartet wird.
Wenn das Spiel beendet ist, z. B. weil die Schlange den Spielfeldrand berührt hat, kann das Spiel
mit der Taste "p" erneut gestartet werden.

Erstelle als erstes eine Funktion ```play()```, in die wir die ```while```-Schleife aus der letzten Aufgabe packen.
Zusätzlich musst du auch wieder ein neues Keyboard-Binding für die Taste "p" erstellen, sodass beim Tastendruck,
die Funktion ```play()``` aufgerufen wird.

Wir brauchen nun noch eine Funktion, damit sich beim erneuten Drücken der Taste "p", die Schlange wieder
auf ihrer Ausgangsposition in der Mitte des Spielfeldes befindet. Schreibe dazu die Funktion ```initialize_board()```.
In der Funktion setzt du die Schlange wieder auf den Ursprung des Koordinatensystems. Die ```snake_head_direction```
wird auch wieder auf die Startrichtung nach rechts gesetzt. Füge abschließend den Aufruf
der Funktion ```initialize_board()``` direkt als erste Zeile in die Funktion ```play()``` ein.

Wenn du möchtest, kannst du noch Hinweise, wie ```print("Starte das Spiel durch Drücken der Taste 'p'")``` 
in dein Programm einfügen. Oder ```print("GAME OVER")```, wenn ein Spiel beendet ist.

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

## 10. Spiel wird beendet, sobald die Schlange sich selbst beißt

In der letzten Aufgabe wird das Spiel noch um die Spielregel erweitert: Die Schlange darf sich nicht
selber in den Schwanz beißen. Du musst dazu bei jeder Bewegung des Kopfes prüfen, ob der Kopf beim vorwärts
bewegen auf einem Schlangenelement landet. Falls die neue Position des Kopfes mit einer Position
der Listenelemente übereinstimmt, wird das Spiel beendet. GAME OVER.

### 10.1 Überprüfen, ob sich die Schlange selbst beißt

In einer der vorherigen Aufgaben habt ihr bereits die Funktion ```check_for_collision_with_turtle_obj(x, y, turtle_obj)```
erstellt. Die Funktion überprüft, ob ```x``` und ```y``` auf der selben Position liegt, wie die Koordinaten des ```turtle_obj```.

Mittlerweile besteht die Schlange nicht mehr aus einem Element, sondern aus einer Liste von Elementen. Deshalb
benötigen wir eine zusätzliche Funktion ```check_for_collision_in_list(x, y, turtle_obj_list)```.
In dieser Funktion gehen wir die gesamte Liste ```turtle_obj_list``` durch. Bei jedem Element wird geprüft, ob dieses
mit den Koordinaten ```x``` und ```y``` kollidiert. Falls es zu einer Kollidierung kommt, geben wir ```False``` zurück.

In der ```move```-Funktion platzieren wir anschließend noch den Aufruf der soeben erstellten Funktion.
Als Liste übergeben wir aber nicht die gesamte Liste, sondern nur die Liste ohne den Kopf.
Schließlich wollen wir nur prüfen, mit welchem Feld der **Kopf** kollidiert.
Du kannst dafür beim Aufruf der Funktion ```snake[1:]``` verwenden. Somit wird eine Liste ohne das erste Element erstellt.
Wenn ```check_for_collision_in_list()``` den Rückgabewert ```True``` liefert (d.h. die Schlange hat sich in den Schwanz
gebissen), verlassen wir die ```move```-Funktion mit ```False```.

**Erweiterung:** Die zwei Funktionen ```check_for_collision_in_list()``` und ```check_for_collision_with_turtle_obj()```
sind fast gleich. Es gilt doppelten Code zu vermeiden. Versuche deswegen die beiden Funktionen zu verketten.
Durch die Verkettung der beiden Funktionen lässt sich doppelter Code vermeiden.

### 10.2 Schlange darf nicht in die Richtung laufen, aus der sie bereits kommt

Als letzte kleine Änderung, passen wir noch die Funktionen ```go_up()```, ```go_down()```, ```go_right()```
und ```go_left()``` an. Bisher konnte die Schlange auch wieder zurück in die Richtung, aus der sie gerade kam.
Wenn die Schlange z.B. nach rechts läuft, kann sie auch auf der Stelle drehen und wieder nach links zurück laufen.
Problematisch wird dies, wenn die Schlange nicht nur aus dem Kopf besteht, sondern aus mehreren Elementen.
Die Schlange würde sich sofort selbst beißen und das Spiel würde beendet werden.

Bevor du in den vier oben genannten Funktionen einen neuen Wert für ```snake_head_direction``` setzt,
kannst du noch überprüfen, aus welcher Richtung die Schlange gerade kommt. Wenn die Schlange mit der
gerade gedrückten Taste in die entgegengesetzte Richtung zurück läuft, wird der Tastendruck ignoriert
und kein neuer Wert für ```snake_head_direction``` gesetzt.

### 10.3 Spielen

Du hast es geschafft. Das Snake-Spiel ist fertig.

Falls es dir zu langweilig wird, bzw. zu einfach ist, kannst du die Geschwindigkeit der Schlange verändern.
Verändere dazu in der Funktion ```play()``` die Zeit, die das Programm "schlafen" soll (```time.sleep()```).
Setze die Zeit z.B. auf ```0.18``` oder ```0.13```. Wie viele Früchte kannst du jetzt noch essen,
bevor sich das Spiel beendet und "GAME OVER" anzeigt wird?

## 11. Erweiterungen

Falls die Teilnehmer schon früher fertig sind können sie das Spiel noch selbstständig erweitern.
Hierzu können sie eigene Ideen einbringen oder einen der nachfolgenden Vorschläge umsetzen.

Mögliche Erweiterungen:
* Auswahl unterschiedlicher Schwierigkeitsstufen beim Spielstart. Die Schlange läuft dementsprechend
schneller oder langsamer. Auswahl kann z.B. über die Konsole erfolgen.
* Live-Counter auf dem Bildschirm anzeigen, wie viele Früchte bereits gegessen wurden.
* Timer einblenden, wie lange das Spiel bereits läuft.
* Eine Mauer als zusätzliches Element einbauen. Nach jeder gegessenen Frucht wird auch eine Mauer auf einem
zufälligen Feld platziert. Die Mauer darf, wie der Spielfeldrand nicht von der Schlange berührt werden.