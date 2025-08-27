import eliminar_notas
import modificar_nota

def inicio():
    while True:
        entrada = input("""
    1. Eliminar
    2. Agregar
    3. Salir""")
        
        if entrada == "1":
            eliminar_notas.inicio()
        elif entrada == "2":
            modificar_nota.inicio()
        elif entrada == "3":
            break
        else:
            print(f"Ingrese una opcion valida, {entrada} no es valido")