from utils.music_theory import CHORD_FORMULAS, COMMON_PROGRESSIONS, NOTES


# Genera un acorde a partir de la nota raiz o tonica y la formula.

def generate_chord(scale, root_note, chord_type):
    formula = CHORD_FORMULAS.get(chord_type)
    if not formula:
        raise ValueError(f"{chord_type} is not a supported chord type.")

    root_index = NOTES.index(root_note) # Usar siempre el índice en NOTES
    chord = []
    for interval in formula:
        index = (root_index + interval) % len(NOTES)
        chord.append(NOTES[index])
    return chord

def generate_chord_progression(scale, progression_name):
    progression_pattern = COMMON_PROGRESSIONS.get(progression_name)
    if not progression_pattern:
        raise ValueError(f"{progression_name} is not a supported progression.")

    chords = []
    for degree in progression_pattern:
        # Corrección CRUCIAL: determinar el tipo de acorde correctamente
        if degree in [1, 4, 5]:
            chord_type = "mayor"
        elif degree in [2, 3, 6]:
            chord_type = "menor"
        elif degree == 7:
            chord_type = "disminuido"
        else:
            raise ValueError(f"Grado {degree} no válido.")

        root_note = scale[degree - 1]
        chord_notes = generate_chord(scale, root_note, chord_type)
        chords.append((root_note + " " + chord_type, chord_notes))

    return chords

