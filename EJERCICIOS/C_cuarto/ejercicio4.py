# Se desea realizar un programa en Python que permita ingresar n números enteros positivos y cuando se
# Ingrese un numero negativo debe mostrar en pantalla el siguiente reporte.

# a. Total de números ingresados
# b. Total de números pares ingresados
# c. Promedio de los números pares
# d. Promedio de los números impares
# e. Cuantos números son menores que 10
# f. Cuantos números están entre 20 y 50
# g. Cuantos números son mayores que 100

def agregarNum(lista:list, numero:int):
    lista.append(numero)

############################################ MENU ###################################################################################################################################################################################################################

def menu():
    titulo="""
    **************************************
    ****** MENU REPORTES *****************
    **************************************
    """

    opciones=['A','B','C','D','E','F','G','H']
    listOpciones=['A. TOTAL NUMEROS INGRESADOS', 'B. NUMEROS PARES INGRESADOS','C. PROMEDIO DE LOS NUMEROS PARES','D. PROMEDIO NUMEROS IMPARES','E. CUANTOS NUMEROS SON MENORES QUE 10','F. CUANTOS NUMEROS ESTAN ENTRE 20 Y 50','G.NUMEROS MAYORES DE 100','H.SALIR']
    print(titulo)
    for item in listOpciones:
        print(item)
    try:
        op=(input('->')).upper()
        if op not in opciones:
            ValueError
    except ValueError:
        print('datos invalidos')
        menu()
    else:
        return op



##################################### INGRESAR DATOS ###############################################################################################################

if __name__ == '__main__':
    numeros = []
    num = 0
    
    while True:
        num = int(input('Ingrese un numero (Ingrese un número negativo para finalizar): '))
        if num >= 0:
            agregarNum(numeros, num)
        else:
            break
    
    menuisrunning = True
    while menuisrunning:
        op = menu()
        
        if op == 'A':
            numTotal = len(numeros)
            print(f'El total de numeros ingresados es: {numTotal}')

        if op == 'B':
            num_pares = 0
            for num in numeros:
                if num % 2 == 0:
                    num_pares += 1
            print(f'El numero total de numeros pares es: {num_pares}')
        
        if op == 'C':
            suma_pares = 0
            contador_pares = 0
            for num in numeros:
                if num % 2 == 0:
                    suma_pares += num
                    contador_pares += 1
            if contador_pares > 0:
                promediop = suma_pares / contador_pares
                print(f'El promedio de los numeros pares es de: {promediop}')
            else:
                print('No hay numeros pares para calcular el promedio.')
                
        if op == 'D':
            suma_impares = 0
            contador_impares = 0
            for num in numeros:
                if num % 2 != 0:
                    suma_impares += num
                    contador_impares += 1
            if contador_impares > 0:
                promedio_impares = suma_impares / contador_impares
                print(f'El promedio de los numeros impares es de: {promedio_impares}')
            else:
                print('No hay numeros impares para calcular el promedio.')

        if op == 'E':
            num_menor_diez = 0
            for num in numeros:
                if num < 10:
                    num_menor_diez += 1
            print(f'Los numeros menores que diez son: {num_menor_diez}')
        
        if op == 'F':
            num_entre_20_y_50 = 0
            for num in numeros:
                if 20 < num < 50:
                    num_entre_20_y_50 += 1
            print(f'El numero total de numeros entre 20 y 50 es: {num_entre_20_y_50}')
        
        if op == 'G':
            num_mayor_100 = 0
            for num in numeros:
                if num > 100:
                    num_mayor_100 += 1
            print(f'El numero total de numeros mayores de 100 es: {num_mayor_100}')
        
        if op == 'H':
            menuisrunning = False