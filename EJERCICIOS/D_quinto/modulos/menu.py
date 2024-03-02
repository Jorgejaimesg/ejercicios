#### MENU PRINCIPAL ###
import os

def menu1():
    options=[1,2,3,4,5]
    optionlist=['1. REGISTRAR CIUDAD', '2. REGISTRAR SISMO', '3. BUSCAR SISMOS POR CIUDAD', '4. INFORME DE RIESGO', '5. SALIR']
    titulo= """
    ++++++++++++++++++++++++++++++++++++++++++++++++
    +++++  PREVENCION DE SISMOS COLOMBIA MENU  +++++
    ++++++++++++++++++++++++++++++++++++++++++++++++
    """
    os.system('cls')

    print(titulo)
    for item in optionlist:
        print (item)
    try:
        op =int(input('-> '))
        if (op not in options):
            menu1()
    except ValueError:
        print ('DATO INVALIDO')
        os.system('pause')
        menu1()
    else:
    
        return op