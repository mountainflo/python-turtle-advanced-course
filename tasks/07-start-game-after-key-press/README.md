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