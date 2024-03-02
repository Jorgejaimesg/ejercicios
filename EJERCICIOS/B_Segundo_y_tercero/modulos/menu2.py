def menu2():
    titulo="""
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++
        ++++++++++++ REPORTES ++++++++++++++++++++++++++
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """
    opciones=['A','B','C','D','E','F']
    listOpciones=['A.PESO IDEAL ', 'B. OBESIDAD GRADO I','C. OBESIDAD GRADO II', 'D. OBESIDAD GRADO III', 'E. SOBREPESO', 'F. REGRESAR AL MENU PRINCIPAL']
    print(titulo)
    print('CUANTOS ESTUDIANES SE ENCUENTRAN EN: ')
    for item in listOpciones:
        print(item)
    try:
        opR=(input('->')).upper()
        if opR not in opciones:
            ValueError
    except ValueError:
        print('datos invalidos')
        menu2()
    else:
        return opR
            