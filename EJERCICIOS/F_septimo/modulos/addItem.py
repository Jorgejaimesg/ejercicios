import os

def add (inventario:dict):
    try:
        codigo=input('Codigo del producto: ').upper()
        if codigo in inventario:
            input('EL PRODUCTO YA SE ENCUENTRA REGISTRADO')
            return
        else:
            nombre=input('nombre del producto: ').upper()
            cantidad=int(0)
            valor_compra =int(input('valor de compra (C/U): '))
            valor_venta=int(input('valor de venta (C/U): '))
            stock_min=int(input('valor minimo de stock: '))
            stock_max=int(input('valor maximo de stock: '))
            proveedor=input('proveedor: ').upper()     
    except ValueError:
        input('VUELVA A INGRESAR LO DATOS, RECUERDE QUE LOS PRECIOS Y LOS VALORES DE STOCK SON NUMERICOS, NO LETRAS')
        os.system('pause')
        add(inventario)
    else:
        pieza={
            'codigo':codigo,
            'nombre':nombre,
            'cantidad':cantidad,
            'valor_compra':valor_compra,
            'valor_venta':valor_venta,
            'stock_min': stock_min,
            'stock_max':stock_max,
            'proveedor':proveedor
            }
        inventario.update({codigo:pieza})