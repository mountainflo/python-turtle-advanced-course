# Python Fortgeschrittenen Kurs

**Kursbeschreibung:**

Der Kurs setzt Grundkenntnisse in Python voraus. Mit Grundkenntnissen sind Variablen, 
Schleifen, Bedingungen und erste einfache Funktionen gemeint. Am Anfang gibt es zur Wiederholung  
nochmals eine Einführung in Funktionen.

Während des Kurses wird das Spiel *Snake* programmiert. Dabei werden Kenntnisse und die Verwendung 
von Listen und Funktionen vertieft. Die Teilnehmer sollen sich auch mit dem Aufbau eines Spiels 
und dessen einzelner Bestandteile auseinandersetzen. Des weiteren sollen die Teilnehmer nach dem 
Kurs für eine Programme selbstständig Informationen aus Dokumentationen ziehen können.

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

Verwendet für diese Aufgabe die Datei [tasks/01-turtle-keyboard-binding-template.py](tasks/01-turtle-keyboard-binding-template.py).
Ersetzt in dieser Datei die ```TODO```-Kommentare mit den richtigen Python-Befehlen.

*Weitere Details, wie die Steuerung über die Tastatur oder das Abfragen und Verändern der Position funktioniert,
findet ihr im Cheatsheet unter: "Position abfragen und verändern" und "Steuerung per Tastatur".*

## 4. Schlange bewegt sich selbstständig vorwärts

In dieser Aufgabe soll sich die Schlange automatisch alle 0.2 Sekunden nach links oder rechts bewegen.
Die Taste, die als letztes gedrückt wurde, gibt die Richtung an, in die sich Schlange bewegt.

Wird zum Beispiel die rechte Pfeiltaste gedrückt, läuft die Schlange nach rechts. 
Die Schlange läuft nun solange nach rechts weiter, bis die linke Pfeiltaste gedrückt wird.

### 4.1 Bildschirm manuell aktualisieren

Bisher hat sich der Bildschirm nach jeder Bewegung der Schlange sofort selbst aktualisiert.
Sobald wir die Position verändert haben, wurde die Schlange auf dem Bildschirm auf die neue Position gesetzt.
Wir möchten nun den Bildschirm mit der Schlange manuell aktualisieren.

Mit ```window.tracer(0)``` können wir die sofortige automatische Aktualisierung des Bildschrims
deaktivieren. Füge ```window.tracer(0)``` unterhalb des Befehls ```window = turtle.Screen()``` ein.

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

1. Erstelle nun eine ```while True```-Schleife, die oberhalb von ```window.mainloop()``` und nach ```window.listen()```
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