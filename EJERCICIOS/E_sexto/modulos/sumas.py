import os
def totalco2(dependencias:dict):
    total=0
    for key,value in dependencias.items():
        print(f'La dependencia {key} consumio {value["total"]} Co2')
        total+=value['total']
    print(f'EL CONSUMO TOTAL DE TODAS LAS DEPENDENCIAS FUE DE: {total}')

def mayorco2(dependencias:dict):
    max=0
    nombre_max=""
    for key,value in dependencias.items():
        if max<value['total']:
            max=value['total']
            nombre_max=value['nombre']
    
    print(f'LA DEPENDENCIA QUE MAS CONSUMIO C02 FUE {nombre_max} CON UN CONSUMO DE {max} KW/H AL MES')
