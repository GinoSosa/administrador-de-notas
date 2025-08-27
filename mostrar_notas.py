import notas
def mostrar_notas_f():
    NEGRO   = "\033[30m"
    ROJO    = "\033[31m"
    VERDE   = "\033[32m"
    AMARILLO= "\033[33m"
    AZUL    = "\033[34m"
    MORADO  = "\033[35m"
    CIAN    = "\033[36m"
    BLANCO  = "\033[37m"
    RESET   = "\033[0m"

    print(ROJO + "Estas son tus notas en materia de la especialidad:")
    print(RESET + f"Patrimonio turistico: {notas.org_turistica_2}")
    print(f"Organizaciones turisticas 2: {notas.org_turistica_2}")
    print(f"Estrategias para las comunicaciones para : {notas.RRHH}")

    print(MORADO + "----------------------------------")

    print(AZUL + "Estas son tus notas en materia troncales:")
    print(RESET + f"Matematicas: {notas.matematicas}")
    print(f"Lengua y Literatura: {notas.lengua}")
    print(f"Historia: {notas.historia}")
    print(f"Fisica: {notas.fisica}")

    print(MORADO + "----------------------------------")

    print(AMARILLO + "Estas son tus notas en materia especiales: ")
    print(RESET + f"Teatro: {notas.teatro}")
    print(f"Ingles: {notas.ingles}")
    print(f"Educacion fisica: {notas.edu_fisica}")