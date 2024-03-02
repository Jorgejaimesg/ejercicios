import os
def menuP():
    titulo="""
    ++++++++++++++++++++++++++++++++++++++
    +++++ SUPER TORNEO DE PING PONG ++++++
    ++++++++++++++++++++++++++++++++++++++
    """
    print(titulo)
    list=[1,2,3,4,5]
    opciones=['1. REGISTRAR JUGADORES','2. VER TABLAS DEL TORNEO','3. INGRESAR PARTIDO','4. RESULTADOS','5. SALIR']
    for item in opciones:
        print(item)
    try:
        op=int(input('->'))
        if op not in list:
            print('OPCION NO DISPONIBLE')
            os.system('pause')
    except ValueError:
        print('DATO INVALIDO')
        os.system('pause')
    else: 
        return op
