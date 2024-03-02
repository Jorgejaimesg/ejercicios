import os
from tabulate import tabulate
def lista(dependencias_ver:dict):
    info = []
    for key,value in dependencias_ver.items():
        info.append(value)
    print(tabulate(info,headers="keys",tablefmt='grid'))