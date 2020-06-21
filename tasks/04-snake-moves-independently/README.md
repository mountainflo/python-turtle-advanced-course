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
