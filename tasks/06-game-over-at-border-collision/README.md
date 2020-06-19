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
