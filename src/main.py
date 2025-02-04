from scales import generate_scale
from chords import generate_chord_progression
from colorama import Fore, Style
from utils.music_theory import COMMON_PROGRESSIONS
from utils.file_handler import save_progression_to_file


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
        print(f"{Fore.GREEN}Escala {scale_type.capitalize()} de {root_note}: {', '.join(scale)}" + Style.RESET_ALL)
    except ValueError as e:
        print(f"Error: {e}") # Maneja errores en la entrada del usuario
        

    # Opción para generar progresión de acordes
    option = input("¿Desea generar una progresión de acordes? (si/no): ").lower()
    if option == "si":
        print("Progresiones disponibles:")
        for i, progression_name in enumerate(COMMON_PROGRESSIONS.keys(), start=1):
            print(f"{Fore.YELLOW}{i}. {progression_name}" + Style.RESET_ALL)  # Muestra opciones numeradas

        try:
            # Permite al usuario seleccionar una progresión usando un número
            choice = int(input("Seleccione el número de la progresión deseada: ")) - 1
            progression_name = list(COMMON_PROGRESSIONS.keys())[choice]
            chords = generate_chord_progression(scale, progression_name)

            print(f"{Fore.GREEN}Progresión generada:" + Style.RESET_ALL)
            for chord_name, chord_notes in chords:
                print(f"{Fore.YELLOW}{chord_name}: {', '.join(chord_notes)}" + Style.RESET_ALL)  # Muestra cada acorde
        except (ValueError, IndexError):
            print(f"{Fore.RED}Error: Selección inválida." + Style.RESET_ALL)  # Maneja errores de entrada inválida
            

    # Preguntar al usuario si desea guardar la progresión
    save_option = input("¿Desea guardar esta progresión en un archivo? (si/no): ").strip().lower()
    if save_option == "si":
        file_name = input("Ingrese el nombre del archivo (con extensión .txt): ").strip()
        scale_info = f"{Fore.GREEN}Escala {scale_type.capitalize()} de {root_note}" + Style.RESET_ALL
        save_progression_to_file(file_name, scale_info, progression_name, chords)




       
if __name__ == "__main__":
    main()