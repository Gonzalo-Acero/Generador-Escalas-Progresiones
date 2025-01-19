from scales import generate_scale
from chords import generate_chord_progression
from utils.music_theory import COMMON_PROGRESSIONS


# Programa principal para generar escalas musicales
def main():
    print("Generador de Escalas Musicales 🎵")
    
    
    # Solicita la nota raíz al usuario
    root_note = input("Ingrese la tonalidad que desee (EJ: C): ").strip().upper()
    
    # Solicita el tipo de escala al usuario
    scale_type = input("Ingrese el tipo de escala (mayor/menor): ").strip().upper()
    
    
    try:
        # Genera la escala y la imprime
        scale = generate_scale(root_note, scale_type)
        print(f"Escala {scale_type.capitalize()} de {root_note}: {', '.join(scale)}")
    except ValueError as e:
        print(f"Error: {e}") # Maneja errores en la entrada del usuario
        

    # Opción para generar progresión de acordes
    option = input("¿Desea generar una progresión de acordes? (si/no): ").lower()
    if option == "si":
        print("Progresiones disponibles:")
        for i, progression_name in enumerate(COMMON_PROGRESSIONS.keys(), start=1):
            print(f"{i}. {progression_name}")  # Muestra opciones numeradas

        try:
            # Permite al usuario seleccionar una progresión usando un número
            choice = int(input("Seleccione el número de la progresión deseada: ")) - 1
            progression_name = list(COMMON_PROGRESSIONS.keys())[choice]
            chords = generate_chord_progression(scale, progression_name)

            print("Progresión generada:")
            for chord_name, chord_notes in chords:
                print(f"{chord_name}: {', '.join(chord_notes)}")  # Muestra cada acorde
        except (ValueError, IndexError):
            print("Error: Selección inválida.")  # Maneja errores de entrada inválida
            
       
if __name__ == "__main__":
    main()