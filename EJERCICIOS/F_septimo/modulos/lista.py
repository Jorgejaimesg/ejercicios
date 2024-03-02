from tabulate import tabulate
import os
def tabular(inventario):
    datos=[]
    for key,value in inventario.items():
        datos.append(value)
    print(tabulate(datos,headers='keys',tablefmt='grid'))