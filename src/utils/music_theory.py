# Lista de notas musicales y sus sostenidos ("#")

NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# NOTES = ["0", "1#", "2", "3#", "4", "5", "6#", "7", "8#", "9", "10#", "11"]

# En la lista estan en cifrado anglosajon para una vista mas sencilla y limpia
# Del lugar donde soy y resido, me las enseñaron con estos nombres:
# DO, RE, MI, FA, SOL, LA, SI, respectivamente (igual estan en el mismo "orden")


# Patrones de intervalos para escalas mayores y menores
SCALES_PATTERNS = {
    "MAYOR": [0, 2, 4, 5, 7, 9, 11],
    "MENOR": [0, 2, 3, 5, 7, 8, 10]
}


# Estos son los "patrones", que siguen las escalas.
# Para que se entienda, imagina un piano, si la escala empieza en X nota, el número representa cuantas
# teclas se omite hasta la siguiente nota pertenenciente a la escala.
# Por EJ: si empezamos en "DO" (o "C"), para cualquiera de las dos escalas se "saltarian" dos notas
# o sea, caeriamos en "RE" (o "D"). NO TE OLVIDES, que al  igual que el piano, tambien se cuentan las teclas negras
# o sostenidos (#) y bemoles (b), por ahora, solo vamos a estar usando SOSTENIDOS
# Estos saltos, son llamados semitonos, y estas en lo correcto, dos semitonos conforman un tono.


# Formulas para construir acordes basicos (de 3 notas o "triadas")

CHORD_FORMULAS = {
    "mayor": [0, 4, 7],             # Intervalos para acorde mayor: raíz, 3ª mayor, 5ª justa
    "menor": [0, 3, 7],             # Intervalos para acorde menor: raíz, 3ª menor, 5ª justa   
    "disminuido": [0, 3, 6],         # Intervalos para acorde disminuido: raíz, 3ª menor, 5ª disminuida
}

# Cada numero representa la "posicion" de la nota en la escala, la nota 0 es la nota raíz del acorde.


# Progresiones de acordes tipicas o mas comunes.

COMMON_PROGRESSIONS = {
    "I-IV-V-I": [1, 4, 5, 1],       # Progresión típica de música clásica y pop
    "ii-V-I": [2, 5, 1],            # Progresión típica de jazz
    "I-V-vi-IV": [1, 5, 6, 4],      # Progresión usada en muchos éxitos pop
}  

# Los numeros romanos representan el "grado" de la escala, o sea, la posicion de la primer nota del acorde, Por EJ: en la primer progresion vemos que 
# empieza con el acorde "I", o sea, que la nota "tonica" es la nota raiz de la escala, pero en el segundo ("IV") la nota "tónica"
# es la cuarta nota de esta misma. Y sí, como te imaginas, depende si el numero romano esta en mayuscula o minuscula, es si el acorde es mayor o menor respectivamente.