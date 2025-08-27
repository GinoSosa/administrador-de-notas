import notas

#define la funcion para modificar las notas de las materias de la especialidad
def mod_especialidad_f():
    mod_especialidad = input("""
1. Patrimonio Turistico
2. Organizaciones Turisticas 2
3. Estrategias para las comunicaciones y relaciones publicas
¿Que materia de la especialidad queres modificar?: """).lower()

    if mod_especialidad == "1":
        mod_patrimonio_turistico = int(input(f"Su lista de notas actual es {notas.org_turistica_2}, que nota quiere agregar (Asegurese que sea un numero entero)"))
        notas.org_turistica_2.append(mod_patrimonio_turistico)
    elif mod_especialidad == "2":
        mod_org_turistica_2 = int(input(f"Su lista de notas actual es {notas.org_turistica_2}, que nota quiere agregar (Asegurese que sea un numero entero)"))
        notas.org_turistica_2.append(mod_org_turistica_2)
    elif mod_especialidad == "3":
        mod_RRHH = int(input(f"Su lista de notas actual es {notas.RRHH}, que nota quiere agregar (Asegurese que sea un numero entero)"))
        notas.org_turistica_2.append(mod_RRHH)  

def mod_troncal_f():
    mod_troncal = input("""
1. Matematicas
2. Lengua y Literatura
3. Historia
4. Fisica
¿Que materia troncal queres modificar?: """).lower()

    if mod_troncal == "1":
        mod_matematicas = int(input(f"Su lista de notas actual es {notas.matematicas}, que nota quiere agregar (Asegurese que sea un numero entero)"))
        notas.matematicas.append(mod_matematicas)
    elif mod_troncal == "2":
        mod_lengua = int(input(f"Su lista de notas actual es {notas.lengua}, que nota quiere agregar (Asegurese que sea un numero entero)"))
        notas.lengua.append(mod_lengua)
    elif mod_troncal == "3":
        mod_historia = int(input(f"Su lista de notas actual es {notas.historia}, que nota quiere agregar (Asegurese que sea un numero entero)"))
        notas.h.append(mod_historia)  
    elif mod_troncal == "4":
        mod_fisica = int(input(f"Su lista de notas actual es {notas.fisica}, que nota quiere agregar (Asegurese que sea un numero entero)"))
        notas.fisica.append(mod_fisica)  

def mod_especiales_f():
    mod_especiales = input("""
1. Teatro
2. Educacion fisica
3. Ingles
¿Que materia de la especialidad queres modificar?: """).lower()

    if mod_especiales == "1":
        mod_teatro = int(input(f"Su lista de notas actual es {notas.teatro}, que nota quiere agregar (Asegurese que sea un numero entero)"))
        notas.teatro.append(mod_teatro)
    elif mod_especiales == "2":
        mod_edu_fisica = int(input(f"Su lista de notas actual es {notas.edu_fisica}, que nota quiere agregar (Asegurese que sea un numero entero)"))
        notas.edu_fisica.append(mod_edu_fisica)
    elif mod_especiales == "3":
        mod_ingles = int(input(f"Su lista de notas actual es {notas.ingles}, que nota quiere agregar (Asegurese que sea un numero entero)"))
        notas.ingles.append(mod_ingles)  


def inicio():
        entrada = input("""¿En que seccion esta la nota que queres modificar?
1. Materia de la especialidad
2. Materia troncal
3. Materia especial
Seleccione una opcion: """).lower()

        if entrada == "1":
            mod_especialidad_f()
        elif entrada == "2":
            mod_troncal_f()
        elif entrada == "3":
            mod_especiales_f()
