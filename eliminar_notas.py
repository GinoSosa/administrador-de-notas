import notas

def especialidad():
    del_especialidad = input("""
1. Patrimonio Turistico
2. Organizacion Turistica 2
3. Estrategias para las comunicaciones y relaciones publicas
¿Que materia de la especialidad queres eliminar una nota?: """)
    
    if del_especialidad == "1":
        print(f"Estas son tus notas en Patrimonio turistico{notas.patrimonio_turistico}")
        notas.patrimonio_turistico.insert(0, 0)
        posicion = int(input("¿Que nota queres eliminar?"))
        notas.patrimonio_turistico.pop(posicion)
        notas.patrimonio_turistico.pop(0)
        print(f"Lista actualizada: {notas.patrimonio_turistico}")
    elif del_especialidad == "2":
        print(f"Estas son tus notas en Organizaciones turisticas 2{notas.org_turistica_2}")
        notas.org_turistica_2.insert(0, 0)
        posicion = int(input("¿Que nota queres eliminar?"))
        notas.org_turistica_2.pop(posicion)
        notas.org_turistica_2.pop(0)
        print(f"Lista actualizada: {notas.org_turistica_2}")
    elif del_especialidad == "2":
        print(f"Estas son tus notas en Organizaciones turisticas 2{notas.RRHH}")
        notas.RRHH.insert(0, 0)
        posicion = int(input("¿Que nota queres eliminar?"))
        notas.RRHH.pop(posicion)
        notas.RRHH.pop(0)
        print(f"Lista actualizada: {notas.RRHH}")

def tronacales():
    del_especialidad = input("""
1. Matematicas
2. Lengua y Literatura
3. Historia
4. Fisica
¿Que materia troncal queres eliminar una nota?: """)
    
    if del_especialidad == "1":
        print(f"Estas son tus notas en Patrimonio turistico{notas.matematicas}")
        notas.matematicas.insert(0, 0)
        posicion = int(input("¿Que nota queres eliminar?"))
        notas.matematicas.pop(posicion)
        notas.matematicas.pop(0)
        print(f"Lista actualizada: {notas.matematicas}")
    elif del_especialidad == "2":
        print(f"Estas son tus notas en Organizaciones turisticas 2{notas.lengua}")
        notas.lengua.insert(0, 0)
        posicion = int(input("¿Que nota queres eliminar?"))
        notas.lengua.pop(posicion)
        notas.lengua.pop(0)
        print(f"Lista actualizada: {notas.lengua}")
    elif del_especialidad == "2":
        print(f"Estas son tus notas en Organizaciones turisticas 2{notas.historia}")
        notas.historia.insert(0, 0)
        posicion = int(input("¿Que nota queres eliminar?"))
        notas.historia.pop(posicion)
        notas.historia.pop(0)
        print(f"Lista actualizada: {notas.historia}")
    elif del_especialidad == "2":
        print(f"Estas son tus notas en Organizaciones turisticas 2{notas.fisica}")
        notas.fisica.insert(0, 0)
        posicion = int(input("¿Que nota queres eliminar?"))
        notas.fisica.pop(posicion)
        notas.fisica.pop(0)
        print(f"Lista actualizada: {notas.fisica}")

def especiales():
    del_especialidad = input("""
1. Teatro
2. Educacion Fisica
3. Ingles
¿Que materia especial queres eliminar una nota?: """)
    
    if del_especialidad == "1":
        print(f"Estas son tus notas en Patrimonio turistico{notas.teatro}")
        notas.teatro.insert(0, 0)
        posicion = int(input("¿Que nota queres eliminar?"))
        notas.teatro.pop(posicion)
        notas.teatro.pop(0)
        print(f"Lista actualizada: {notas.teatro}")
    elif del_especialidad == "2":
        print(f"Estas son tus notas en Organizaciones turisticas 2{notas.edu_fisica}")
        notas.edu_fisica.insert(0, 0)
        posicion = int(input("¿Que nota queres eliminar?"))
        notas.edu_fisica.pop(posicion)
        notas.edu_fisica.pop(0)
        print(f"Lista actualizada: {notas.edu_fisica}")
    elif del_especialidad == "2":
        print(f"Estas son tus notas en Organizaciones turisticas 2{notas.ingles}")
        notas.ingles.insert(0, 0)
        posicion = int(input("¿Que nota queres eliminar?"))
        notas.ingles.pop(posicion)
        notas.ingles.pop(0)
        print(f"Lista actualizada: {notas.ingles}")

def inicio():
    while True:
        entrada = input("""
1. Materias de la especialidad
2. Materias troncales
3. Materias especiales
4. Salir
¿Que materias quiere eleminar notas?""")
        
        if entrada == "1":
            especialidad()
        elif entrada == "2":
            tronacales()
        elif entrada == "3":
            especiales()
        elif entrada == "4":
            break
        else:
            print(f"Ingrese una opcion valida {entrada} no es valido")
