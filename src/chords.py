from utils.music_theory import CHORD_FORMULAS, COMMON_PROGRESSIONS


# Genera un acorde a partir de la nota raiz o tonica y la formula.

def generate_chord(scale, root_index, chord_type):
    formula = CHORD_FORMULAS.get(chord_type)
    if not formula:
        raise ValueError(f"{chord_type} is not a supported chord type.")
    
    
    chord = [scale[(root_index + interval) % len(scale)] for interval in formula]
    return chord


# Genera una progresion de acorde a partir de una escala y una progresion predefinida

def generate_chord_progression(scale, progression_name):
    progression_pattern = COMMON_PROGRESSIONS.get(progression_name)
    if not progression_pattern:
        raise ValueError(f"{progression_name} is not a supported progression.")
    
    
    chords = []
    for degree in progression_pattern:
        chord_type = "mayor" if degree in  [1, 4, 5] else "menor" # Simplificacion basica
        chord = generate_chord(scale, degree - 1, chord_type)
        chords.append((f"{degree} ({chord_type})", chord))
        
    return chords