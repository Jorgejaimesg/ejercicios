import os
def crit(inventario:dict):
    for key,values in inventario.items():
        if values['stock_min']>=values['cantidad']:
            print(f'{key}. {values["nombre"]}')