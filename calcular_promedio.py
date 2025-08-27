import notas

#promedio materias de la especialidad
def patrimonio_turistico_prom_d():
    return (sum(notas.org_turistica_2)) / len(notas.org_turistica_2)

def org_turistica_2_prom_d():
    return (sum(notas.org_turistica_2)) / len(notas.org_turistica_2)

def RRHH_prom_d():
    return (sum(notas.RRHH)) / len(notas.RRHH)

#promedio materias troncales
def matematicas_prom_d():
    return (sum(notas.matematicas)) / len(notas.matematicas)

def lengua_prom_d():
    return (sum(notas.lengua)) / len(notas.lengua)

def historia_prom_d():
    return (sum(notas.historia)) / len(notas.historia)

def fisica_prom_d():
    return (sum(notas.fisica)) / len(notas.fisica)

#promedio materias especiales
def teatro_prom_d():
    return (sum(notas.teatro)) / len(notas.teatro)

def edu_fisica_prom_d():
    return (sum(notas.edu_fisica)) / len(notas.edu_fisica)

def ingles_prom_d():
    return (sum(notas.ingles)) / len(notas.ingles)
