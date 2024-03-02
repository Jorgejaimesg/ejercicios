import modulos.menuCategorias as mc


####### VALIDACION 5 INSCRITOS E INGRESO DE DATOS#########################################################################################################################

def validacion(torneo:dict,categoria):
    if len(torneo[categoria])<5:
                print(f'NO SE PUEDE REALIZAR EL TORNEO, MINIMO SE NECESITAN 5 PARTICIPANTES Y SOLO SE HAN INSCRITO {len(torneo[categoria])} EN LA CATEGORIA {categoria}')
                mc.os.system('pause')
    else:
        for key,value in torneo[categoria].items():
            print (f'{key}. {value["nombre"]}')
        isValid=True
        while isValid:
            p_1=(input('Dijite el codigo del participante #1: ')).upper()
            p_2=(input('Dijite el codigo del participante #2: ')).upper()
            if (p_1 == p_2) or (p_1 not in torneo[categoria])or(p_2 not in torneo[categoria]):
                print('datos invalidos')
                mc.os.system('pause')
            else:
                isValid=False
        puntos_1=solicitar_puntos(torneo,categoria,p_1)
        puntos_2=solicitar_puntos(torneo,categoria,p_2)

######## EVALUO QUIEN GANA ###################################################################################################################################

        if puntos_1>puntos_2:
             actualizartablas(torneo[categoria][p_1],puntos_2,puntos_1,'G')
             actualizartablas(torneo[categoria][p_2],puntos_1,puntos_2,'P')
        if puntos_1<puntos_2:
             actualizartablas(torneo[categoria][p_1],puntos_2,puntos_1,'P')
             actualizartablas(torneo[categoria][p_2],puntos_1,puntos_2,'G')

########### ACTUALIZO LA TABLA ###################################################################################################################################
def actualizartablas(torneo,puntosContra,puntosaFavor,resultado):
    torneo['PJ']+=1
    torneo['PA']+=(puntosaFavor-puntosContra)

    if resultado == 'G':
        torneo['PG']+=1
        torneo['TP']+=2
    else:
        torneo['PP']+=1       
              
########### COMPRUEBO SI EL NUMERO DE PUNTOS ES UN NUMERO ###################################################################################################################################
def solicitar_puntos(torneo,categoria,id):
            while True:
                    try:
                        opcion = int(input(f"cuantos puntos anoto el participante {torneo[categoria][id]['nombre']}: "))
                        return opcion
                    except ValueError:
                        print('datos invalidos')
                        mc.os.system('pause')
                        mc.os.system('cls')
############# FUNCION PRINCIPAL DEPENDIENDO DE LA CATEGORIA #################################################################################################################################
def addMatch(torneo:dict):
    op=mc.categoria()
    if op==1:##novato
        validacion(torneo,"novato")        
    if op==2:##intermedio
        validacion(torneo,"intermedio")
    if op==3:##avanzado
        validacion(torneo,"avanzado")