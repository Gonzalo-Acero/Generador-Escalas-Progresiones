from utils.music_theory import NOTES, SCALES_PATTERNS
from colorama import Fore, Style

# Genera una escala musical a partir de la nota "raíz" y el tipo de escala

def generate_scale(root, scale_type):
   
   root = root.upper()  # Asegurarnos de manejar mayúsculas/minúsculas
   if root not in NOTES:
        raise ValueError(f"{Fore.RED}{root} no es una nota válida. Usa notas como C, D#, etc." + Style.RESET_ALL)
    
      
   formula = SCALES_PATTERNS.get(scale_type)
   if not formula:
        raise ValueError(f"{Fore.RED}{scale_type} no es un tipo de escala válido." + Style.RESET_ALL)
    
   root_index = NOTES.index(root)
   scale = [NOTES[(root_index + interval) % len(NOTES)] for interval in formula]
    
    
   return scale
   
