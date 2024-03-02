import os
def menuP():
    os.system('cls')
    title="""
    +++++++++++++++++++++++++++++++++++++++++
    ++++++++ CO2 ++++++++++++++++++++++++++++
    +++++++++++++++++++++++++++++++++++++++++
    """
    print(title)
    opciones=[1,2,3,4,5,6]
    listOpciones=['1. REGISTRAR DEPENDENCIA','2. VER DATOS','3. REGISTRAR CONSUMO','4. VER C02 PRODUCIDO','5. DEPENDENCIA QUE PRODUCE MAYOR C02','6. SALIR']
    for item in listOpciones:
        print(item)
    try:
        op=int(input('->'))
        if op not in opciones:
            print('OPCION INVALIDA')
            menuP()
    except ValueError:
        print('DIGITE EL NUMERO DE LA OPCION, NO LETRAS')
        menuP()
    else:
        return op