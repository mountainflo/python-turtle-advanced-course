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

*Weitere Details, wie die Steuerung über die Tastatur oder das Abfragen und Verändern der Position funktioniert,
findet ihr im Cheatsheet unter: "Position abfragen und verändern" und "Steuerung per Tastatur".*

