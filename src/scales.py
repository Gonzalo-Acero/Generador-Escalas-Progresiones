from utils.music_theory import NOTES, SCALES_PATTERNS


# Genera una escala musical a partir de la nota "raíz" y el tipo de escala

def generate_scale(root_note, scale_type):
    # Valida que la nota raíz sea válida
    if root_note not in NOTES:
        raise ValueError(f"{root_note} is not valid note.")
    
    # Valida que el tipo de escala sea soportado y mormaliza el tipo de escala a minúsculas para validar correctamente
    scale_type = scale_type.lower()
    if scale_type not in SCALES_PATTERNS:
        raise ValueError(f"{scale_type} is not a supported scale type.")
    
    
    # Obtiene el patrón de intervalos para el tipo de escala
    pattern = SCALES_PATTERNS[scale_type]
    scale = []
    start_index = NOTES.index(root_note)
    
    
    # Construye la escala siguiendo el patrón de intervalos
    for step in pattern:
        scale.append(NOTES[start_index])
        start_index = (start_index + step) % len(NOTES) # Asegura que sea cíclico
        
        
    return scale