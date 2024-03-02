
def bucarCategoria(estudiantes:dict, tipo:str):
    tipoMax=0
    for estudiante in estudiantes.values():
        if estudiante['categoria']==tipo:
            tipoMax+=1
            return tipoMax
        