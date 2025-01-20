import os


# Guarda una progresion de acordes en un archivo de texto

def save_progression_to_file(file_name, scale_info, progression_name, chords):
    
    # Define la carpeta donde se guardarán las progresiones
    folder_name = "Progresiones Guardadas"
    
    try:
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
        
        print(f"Progresión guardada en '{full_path}' con éxito.")
    except Exception as e:
        print(f"Error al guardar la progresión: {e}")