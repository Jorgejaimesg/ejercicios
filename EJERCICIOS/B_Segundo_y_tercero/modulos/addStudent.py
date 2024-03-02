import os
def newStudent(estudiantes: dict):
    isTheSame=True
    while isTheSame==True:
        nombre=input('Ingrese el nombre del estudiante que quiere añadir: ').upper()
        for estudiante in estudiantes.values():
            if estudiante['nombre']==nombre:
                print('el eestudiante ya se encuentra registrado:')
                os.system('pause')
                os.system('cls')
                break
                
        else:
            isTheSame=False
        
    edad=comprobar('INGRESE LA EDAD DEL ESTUDIANTE: ')
    altura=comprobar('INGRESE LA ALTURA DEL ESTUDIANTE: ')
    peso=comprobar('INGRESE EL PESO DEL ESTUDIANTE: ')
    imc=float(peso/(altura*altura))
    if (imc >= 18.5)and(imc<25):
        categoria='normal'
    elif (imc >= 25)and(imc<30):
        categoria='sobrepeso'
    elif (imc >= 30)and(imc<35):
        categoria='obesidad 1'
    elif (imc >= 35)and(imc<40):
        categoria='obesidad 2'
    elif (imc >= 40):
        categoria='obesidad 3'
    else:
        categoria='no aplica'

    estudiante={
        'nombre':nombre,
    'edad':edad,
    'altura':altura,
    'peso':peso,
    'imc':imc,
    'categoria':categoria,
    }

    estudiantes.update({(len(estudiantes)+1):estudiante})

def comprobar(msg):
    try:
        dato=float(input(msg))
        if dato <0:
            ValueError
    except ValueError:
        print('dato invalido, deben ser numeros')
        comprobar(msg)
    else:
        return dato
