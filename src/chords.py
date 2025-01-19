from utils.music_theory import CHORD_FORMULAS, COMMON_PROGRESSIONS


# Genera un acorde a partir de la nota raiz o tonica y la formula.

def generate_chord(scale, root_index, chord_type):
    formula = CHORD_FORMULAS.get(chord_type)        # Obtiene la fórmula del acorde
    if not formula:
        raise ValueError(f"{chord_type} is not a supported chord type.")        # Maneja errores de tipo desconocido
    
    
    # Genera el acorde aplicando los intervalos de la fórmula
    
    chord = [scale[(root_index + interval) % len(scale)] for interval in formula]
    return chord


# Genera una progresion de acordes a partir de una escala y una progresion predefinida

def generate_chord_progression(scale, progression_name):
    progression_pattern = COMMON_PROGRESSIONS.get(progression_name)     # Obtiene el patrón de grados
    if not progression_pattern:
        raise ValueError(f"{progression_name} is not a supported progression.")     # Maneja errores de progresión desconocida
    
    
    chords = []
    for degree in progression_pattern:
        chord_type = "mayor" if degree in  [1, 4, 5] else "menor"       # Determina el tipo de acorde según el grado
        chord = generate_chord(scale, degree - 1, chord_type)           # Genera el acorde
        chords.append((f"{degree} ({chord_type})", chord))              # Añade el acorde a la lista
        
    return chords