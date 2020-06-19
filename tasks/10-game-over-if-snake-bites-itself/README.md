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