
import modulos.menuCategorias as mc
from tabulate import tabulate
def a(torneo:dict,categoria,info):
    print(f"""
        +++++++++++++++++++++++++++++++++++++++++++
        ++++++++++ LISTA {categoria}s +++++++++++++++++
        +++++++++++++++++++++++++++++++++++++++++++
        """)
    if len(torneo[categoria])==0:
            print(f'NO HAY NINGUN PARTICIPANTE REGISTRADO EN {categoria}s')
            mc.os.system('pause')
    else:
        for key,value in torneo[categoria].items():
            info.append(value)
        print(tabulate(info,headers="keys",tablefmt='grid'))
        mc.os.system('pause')

def lista(torneo:dict):
    info = []
    op=mc.categoria()
    if op==1:
        categoria='novato'
        a(torneo,categoria,info)
    if op==2:
        categoria='intermedio'
        a(torneo,categoria,info)
    if op==3:
        categoria='avanzado'
        a(torneo,categoria,info)