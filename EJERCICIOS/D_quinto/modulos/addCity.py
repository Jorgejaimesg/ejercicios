
import os

################# AGREGAR CIUDAD NUEVA ###########################

def ciudad(ciudades:list):
    if len(ciudades)<=5:
        nombre=input('ingrese el nombre de la ciudad: ')
        ciudades.append([nombre])
    else:
        print('ya no hay capacidad para mas ciudades')
        os.system('pause')

################ AGREGAR SISMOS ################################################

def sismo(ciudades:list,n):
    print(f'recuerde que solo se pueden ingresar {n} sismos por ciudad')
    for idx, item in enumerate(ciudades):  
        print(f'{idx+1}. {str(item[0]).upper()}')
    ciudad=int(input('ingrese el nombre de la ciudad: '))
    for idx,item in enumerate(ciudades):
        if item[0]==ciudades[ciudad-1][0]:
            if len(item)<=(n+1):
                sismo=float(input('ingrese el valor del sismo'))
                item.append(sismo)
                print(f'le quedan {(n+1)-(len(item))} sismos por ingresar a {item[0]}')
                os.system('pause')
            else:
                print(f'ya no hay capacidad para mas datos de sismos en {item[0]}')
                os.system('pause')
################ BUSCAR SISMOS ############################################################3

def buscarSismos(ciudades:list):
    for idx, item in enumerate(ciudades):  
        print(f'{idx+1}. {str(item[0]).upper()}')
    ciudad=int(input('ingrese el nombre de la ciudad: '))
    for idx,item in enumerate(ciudades):
        if item[0]==ciudades[ciudad-1][0]:
            print(item)

############# INFORMES #######################################################
            
def informes(ciudades:list, ciudad: str):
    for idx,item in enumerate(ciudades):
        if item[0]==ciudades[ciudad-1][0]:
            suma=sum(item[1:])
            cantidad=(len(item)-1)
            promedio=suma/cantidad
    return promedio

######### COMPROBACION #####################################################
def comprobar(ciudades:list):
    primeraLista = len(ciudades[0])
    for listas in ciudades[1:]:
        if len(listas) != primeraLista:
            return False
    return True