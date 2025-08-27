import mostrar_notas
import mostrar_promedio
import elejir_modificar_o_eliminar_nota

while True:
    print("-------------------------")
    entrada = input("""Bienvenido al gestor de notas:
    1. Ver notas
    2. Promedio
    3. Promedio materias de la especialidad
    4. Promedio materias troncales
    5. Promedio materias especiales
    6. Ingresar o eliminar notas
    7. Salir
    ¿Que queres hacer?: """).lower()

    if entrada in ("1","ver notas"):
        mostrar_notas.mostrar_notas_f()
    elif entrada in ("2","promedio"):
        mostrar_promedio.mostrar_promedio_f()
    elif entrada in ("3","promedio materias de la especialidad"):
        mostrar_promedio.prom_especialidad()
    elif entrada in ("4","promedio materias troncales"):
        mostrar_promedio.prom_troncales()
    elif entrada in ("5","promedio materias especiales"):
        mostrar_promedio.prom_especiales()
    elif entrada in ("6","ingresar notas"):
        elejir_modificar_o_eliminar_nota.inicio()
    elif entrada in ("7","salir","exit"):
        print("Saliendo...")
        break
    else:
        print("Ingrese un valor valido")
