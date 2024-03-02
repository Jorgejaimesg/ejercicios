import modulos.menuCategorias as mc
def reportes(torneo:dict):
    op=mc.categoria()
    if op==1:
        ganador(torneo,"novato")
    elif op==2:
        ganador(torneo,"intermedio")
    else:
        ganador(torneo,"avanzado")

######################################################

def ganador(torneo:dict,categoria):
    max_favor=0
    max_puntos=0
    max_nombre=("")
    for key,value in torneo[categoria].items():
        if max_puntos<value['TP']:
            max_favor=value['PA']
            max_puntos=value['TP']
            max_nombre=(value['id'],value['nombre'])
        elif max_puntos==value['TP']:
            if max_favor<value['PA']:
                max_favor=value['PA']
                max_puntos=value['TP']
                max_nombre=(value['id'],value['nombre'])
    print(f'(el ganador de la {categoria} es {max_nombre} con {max_puntos} puntos y {max_favor} puntos a favor ')
    mc.os.system('pause')