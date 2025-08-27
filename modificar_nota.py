import notas

def mod_especialidad_f():
   mod_especialidad = input("""¿Que materia de la especialidad queres modificar?
1. Patrimonio Turistico
2. Organizaciones Turisticas 2
3. Estrategias para las comunicaciones y relaciones publicas""").lower()
   if mod_especialidad == "1":
        mod_patrimonio_turistico = int(input(f"Su lista de notas actual es {notas.patrimonio_turistico}, que nota quiere agregar (Asegurese que sea un numero entero)"))
        notas.patrimonio_turistico.append(mod_patrimonio_turistico)


def mod_troncal():
    a = input(2)
def mod_especiales():
    a = input(3)


def inicio():
        entrada = input("""¿En que seccion esta la nota que queres modificar?
1. Materia de la especialidad
2. Materia troncal
3. Materia especial
Seleccione una opcion: """).lower()

        if entrada == "1":
            mod_especialidad_f()
        elif entrada == "2":
            mod_troncal()
        elif entrada == "3":
            mod_especiales()
