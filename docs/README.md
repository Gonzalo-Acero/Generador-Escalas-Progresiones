# Archivo Principal de Documentación


### Teoria musical basica implementada

*music_theory.py*
~~~
NOTES = ["C", "C#", "D", "D#", "E", "F#", "G", "G#", "A", "A#", "B"]

En la lista estan en cifrado anglosajon para una vista mas sencilla y limpia
Del lugar donde soy y resido, me las enseñaron con estos nombres:
DO, RE, MI, FA, SOL, LA, SI, respectivamente (igual estan en el mismo "orden")

SCALES_PATTERNS = {
    "mayor": [2, 2, 1, 2, 2, 2, 1],
    "menor": [2, 1, 2, 2, 1, 2, 2]
}

Estos son los "patrones", que siguen las escalas.
Para que se entienda, imagina un piano, si la escala empieza en X nota, el número representa cuantas
teclas se omite hasta la siguiente nota pertenenciente a la escala.
Por EJ: si empezamos en "DO" (o "C"), para cualquiera de las dos escalas se "saltarian" dos notas o sea, caeriamos en "RE" (o "D"). NO TE OLVIDES, que al  igual que el piano, tambien se cuentan las teclas negras
o sostenidos (#) y bemoles (b), por ahora, solo vamos a estar usando SOSTENIDOS. Estos saltos, son llamados semitonos, y estas en lo correcto, dos semitonos conforman un tono.
~~~