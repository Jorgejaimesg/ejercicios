import os
def menuStock ():
    opciones=[1,2]
    listopciones=['1. AÑADIR PRODUCTOS', '2. QUITAR PRODUCTOS']
    for item in listopciones:
        print(item)
    try:
        op=int(input('->'))
        if op not in opciones:
            print('ESA OPCION NO SE ENCUENTRA EN LA LISTA')
    except ValueError:
        print('DATO INVALIDO')
    else:
        return op

def manipularStock(inventario:dict):
    print(f' ESTOS SON LOS CODIGOS INSCRITOS {inventario.keys()}')
    codigo=input('ingrese el codigo del producto: ').upper()
    for item,value in inventario.items():
            if item==codigo:
                ops=int(menuStock())
                if ops==1:
                            try:
                                añadir=int(input(f'cantidad de productos a AÑADIR a {inventario[codigo]["nombre"]} : '))
                                if inventario[codigo]["cantidad"]+añadir>inventario[codigo]['stock_max']:
                                    print(f'no se puede ingresar esa cantidad de productos, debido a que la cantidad maxima que estan permitidas recibir en este momento es: {(inventario[codigo]["stock_max"])-(inventario[codigo]["cantidad"])}')
                                else:
                                    inventario[codigo]['cantidad']+=añadir
                                    return
                            except ValueError:
                                print('LA CANTIDAD DEBE DARSE EN NUMEROS')
                                return
                if ops ==2:
                    try:
                        añadir=int(input(f'cantidad de productos que desea ELIMINAR a {inventario[codigo]["nombre"]} : '))
                        if inventario[codigo]['cantidad']-añadir<0:
                            print(f'no se pueden retirar esa cantidad de productos, debido a que solo se cuenta con: {(inventario[codigo]["cantidad"])} {inventario[codigo]["nombre"]}s')
                        else:
                            inventario[codigo]['cantidad']+=(-añadir)
                            if inventario[codigo]["cantidad"]-añadir<inventario[codigo]['stock_min']:
                                print(f'ALERTA!!!! tienes una cantidad de {inventario[codigo]["nombre"]} menor que el stock minimo permitido, LLAMA AL PROVEEDOR')
                            return
                    except ValueError:
                        print('LA CANTIDAD DEBE DARSE EN NUMEROS')
                        return       
    else:
        print('ESE PRODUCTO NO SE ENCUENTRA REGISTRADO')

            
                