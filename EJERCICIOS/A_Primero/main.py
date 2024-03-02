import os
if __name__=='__main__':
    titulo="""
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        ++++++++++++ SUMA ENTEROS POSITIVOS ++++++++++++++++++++
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """
def comprobar(msg: str):

    while True:
        try:
                numero=int(input(msg))
                if numero<0:
                    print('el valores es negativo')
                else:
                    return numero
        except ValueError:
            print('datos invalidos')
    


print(titulo)
n1=comprobar('INGRESE EL PRIMER NUMERO: ')
n2=comprobar('INGRESE EL SEGUNDO NUMERO: ')
n3=comprobar('INGRESE EL TERCER NUMERO: ')
sumaT=n1+n2+n3
print(f'LA SUMA DE LOS 3 NUMEROS ES IGUAL A: {sumaT}')

