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
