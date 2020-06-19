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

Verwendet für diese Aufgabe die Datei [03-turtle-keyboard-binding-template.py](03-turtle-keyboard-binding-template.py).
Ersetzt in dieser Datei die ```TODO```-Kommentare mit den richtigen Python-Befehlen.

*Weitere Details, wie die Steuerung über die Tastatur oder das Abfragen und Verändern der Position funktioniert,
findet ihr im Cheatsheet unter: "Position abfragen und verändern" und "Steuerung per Tastatur".*
