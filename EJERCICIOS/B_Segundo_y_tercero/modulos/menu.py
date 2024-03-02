
def menu():
    titulo="""
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++
        ++++++++++++ CALCULO DEL IMC ++++++++++++++++++++++++++
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """
    opciones=[1,2,3,4]
    listOpciones=['1. AÑADIR NUEVO ESTUDIANTE', '2. VER LISTA DE ESTUDIANTES','3. REPORTES', '4.SALIR']
    print(titulo)
    for item in listOpciones:
        print(item)
    try:
        op=int(input('->'))
        if op not in opciones:
            ValueError
    except ValueError:
        print('datos invalidos')
        menu()
    else:
        return op
            