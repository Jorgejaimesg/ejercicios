import os
from tabulate import tabulate
def list(estudiantes:dict):
    info = []
    for key,value in estudiantes.items():
        info.append(value)
    print(tabulate(info,headers="keys",tablefmt='grid'))