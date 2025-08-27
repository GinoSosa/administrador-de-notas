import calcular_promedio

NEGRO   = "\033[30m"
ROJO    = "\033[31m"
VERDE   = "\033[32m"
AMARILLO= "\033[33m"
AZUL    = "\033[34m"
MORADO  = "\033[35m"
CIAN    = "\033[36m"
BLANCO  = "\033[37m"
RESET   = "\033[0m"

contador = 0

while contador < 1:

    def mostrar_promedio_f():
        #promedio materias de la especialidad
        print(ROJO + f"Estos son los promedios de las materia de la especialidad")
        print(RESET + f"Este es tu promedio de Patrimonio turistico: {calcular_promedio.patrimonio_turistico_prom_d()}")
        print(f"Este es tu promedio de Organizacion turitica: {calcular_promedio.org_turistica_2_prom_d()}")
        print(f"Este es tu promedio de Estrategias para las comunicacicones y relaciones publicas: {calcular_promedio.RRHH_prom_d()}")

        print(MORADO + "----------------------------------")

        #promedio materias troncales
        print(AZUL + "Estos son los promedios de las materia troncales")
        print(RESET + f"Este es tu promedio de Matematicas: {calcular_promedio.matematicas_prom_d()}")
        print(f"Este es tu promedio de Lengua y Literatura: {calcular_promedio.lengua_prom_d()}")
        print(f"Este es tu promedio de Historia: {calcular_promedio.historia_prom_d()}")
        print(f"Este es tu promedio de Fisica: {calcular_promedio.fisica_prom_d()}")

        print(MORADO + "----------------------------------")
        
        #promedio materias especiales
        print(AMARILLO + "Estos son los promedios de las materia especiales")
        print(RESET + f"Este es tu promedio de Teatro: {calcular_promedio.teatro_prom_d()}")
        print(f"Este es tu promedio de Ingles: {calcular_promedio.ingles_prom_d()}")
        print(f"Este es tu promedio de Educacion fisica: {calcular_promedio.edu_fisica_prom_d()}")
        contador += 1

    def prom_especialidad():
        print(ROJO + f"Estos son los promedios de las materia de la especialiad")
        print(RESET + f"Este es tu promedio de Patrimonio turistico: {calcular_promedio.patrimonio_turistico_prom_d()}")
        print(f"Este es tu promedio de Organizacion turitica: {calcular_promedio.org_turistica_2_prom_d()}")
        print(f"Este es tu promedio de Estrategias para las comunicaicones y relaciones publicas: {calcular_promedio.RRHH_prom_d()}")
        contador += 1

    def prom_troncales():
        print(AZUL + "Estos son los promedios de las materia troncales")
        print(RESET + f"Este es tu promedio de Matematicas: {calcular_promedio.matematicas_prom_d()}")
        print(f"Este es tu promedio de Lengua y Literatura: {calcular_promedio.lengua_prom_d()}")
        print(f"Este es tu promedio de Historia: {calcular_promedio.historia_prom_d()}")
        print(f"Este es tu promedio de Fisica: {calcular_promedio.fisica_prom_d()}")
        contador += 1

    def prom_especiales():
        print(AMARILLO + "Estos son los promedios de las materia especiales")
        print(RESET + f"Este es tu promedio de Teatro: {calcular_promedio.teatro_prom_d()}")
        print(f"Este es tu promedio de Ingles: {calcular_promedio.ingles_prom_d()}")
        print(f"Este es tu promedio de Educacion fisica: {calcular_promedio.edu_fisica_prom_d()}")
        contador += 1

contador -= 4