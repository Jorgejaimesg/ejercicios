import os

def menuPrincipal ():
    os.system('cls')
    titulo=str("""
    +++++++++++++++++++++++++++++++++++++++++++++++
    ++++++++++++++++ INVENTARIO +++++++++++++++++++
    +++++++++++++++++++++++++++++++++++++++++++++++
    """)
    print(titulo)
    opciones=[1,2,3,4,5,6]
    listOpciones=['1. REGISTRAR PRODUCTO','2. VER PRODUCTOS','3. ENTRADA O SALIDA DE PRODUCTOS','4. INFORME DE PRODUCTOS','5. GANANCIA POTENCIAL','6. SALIR']

    for item in listOpciones:
        print(item)
    try:
        op=int(input('->'))
        if op not in opciones:
            print('Esa opcion no se encuentra disponible')
            os.system('pause')
            menuPrincipal()
    except ValueError:
        print('DATOS INVALIDOS')
        os.system('pause')
        menuPrincipal()
    else:
        return op