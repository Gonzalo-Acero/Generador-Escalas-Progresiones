import os
import re # Para validar el nombre de los archivos a guardar o exportar
from colorama import Fore, Style

# Guarda una progresion de acordes en un archivo de texto

def save_progression_to_file(file_name, scale_info, progression_name, chords):
    
    # Define la carpeta donde se guardarán las progresiones
    folder_name = "Progresiones Guardadas"
    
    try:
        
        # Valida y ajusta el nombre del archivo
        
        if not file_name.endswith(".txt"):
            file_name += ".txt" # Agrega extension .txt si no esta incluida por el usuario
            
        # Remueve caracteres no permitidos en nombres de archivos
        file_name = re.sub(r'[<>:"/\\|?*]', '', file_name)
        
        # Crea la carpeta si no existe
        os.makedirs(folder_name, exist_ok=True)
        
        # Define la ruta completa del archivo
        full_path = os.path.join(folder_name, file_name)
        
        # Escribe la información en el archivo
        with open(full_path, 'w') as file:
            file.write(f"{scale_info}\n")
            file.write(f"Progresión: {progression_name}\n")
            file.write("Acordes:\n")
            for chord_name, chord_notes in chords:
                file.write(f"{chord_name}: {', '.join(chord_notes)}\n")
        
        print(f"{Fore.GREEN}Progresión guardada exitosamente en: {full_path}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error al guardar la progresión: {e}{Style.RESET_ALL}")