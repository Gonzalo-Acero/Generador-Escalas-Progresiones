from scales import generate_scale


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
        
        
if __name__ == "__main__":
    main()