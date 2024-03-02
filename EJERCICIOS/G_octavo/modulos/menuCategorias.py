import os
def categoria():
    title="""
    +++++++++++++++++++++++++++++++++++++++++
    ++++++ ELIJA LA CATEGORIA +++++++++++++++
    +++++++++++++++++++++++++++++++++++++++++
    """
    print(title)
    list=[1,2,3]
    options=['1. NOVATO','2. INTERMEDIO','3. AVANZADO']
    for item in options:
        print(item)
    try:
        op=int(input('->'))
        if op not in list:
            print('CATEGORIA NO DISPONIBLE')
            os.system('pause')
    except ValueError:
        print('DATO INVALIDO')
        os.system('pause')
    else:
        os.system('cls')
        return op

