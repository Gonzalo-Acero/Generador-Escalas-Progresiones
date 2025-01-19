from scales import generate_scale
from chords import generate_chord_progression


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
        

    # Preguntar al usuario si quiere que se genere una progresion de acordes

    option = input("¿Desea generar una progresion de acordes? (si/no): ").lower()
    if option == "si":
        print("Progresiones disponibles: I-IV-V-I, ii-V-I, I-V-vi-IV")
        progression_name = input("Ingrese el nombre de la progresion deseada: ")
        try:
            chords = generate_chord_progression(scale, progression_name)
            print("Progresion generada:")
            for chord_name, chord_notes in chords:
                print(f"{chord_name}: {', '.join(chord_notes)}")
        except ValueError as e:
            print(f"Error: {e}")
            return
            
       
if __name__ == "__main__":
    main()