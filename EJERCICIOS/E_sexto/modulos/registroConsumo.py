import os

def menu1():
    os.system('cls')
    titulo="""
    ++++++++++++++++++++++++++++++++++++++++
    ++++++ REGISTRO DE CONSUMO +++++++++++++
    ++++++++++++++++++++++++++++++++++++++++"""
    print(titulo)
    list=[1,2]
    options=['1. ELECTRICIDAD','2. TRANSPORTE']
    for item in options:
        print(item)
    try:
        op=int(input('->'))
        if op not in list:
            print('OPCION NO DISPONIBLE')
            os.system('pause')
    except ValueError:
        print('DATO INVALIDO')
        os.system('pause')
    else:
        return op

###########################################################################################################

def menu2():
    os.system('cls')
    titulo="""
    ++++++++++++++++++++++++++++++++++++++++
    ++++++ REGISTRO DE ELECTRICIDAD ++++++++
    ++++++++++++++++++++++++++++++++++++++++"""
    print(titulo)
    list=[1,2]
    options=['1. ELECTRODOMESTICOS','2. FACTURA GENERAL']
    for item in options:
        print(item)
    try:
        op=int(input('->'))
        if op not in list:
            print('OPCION NO DISPONIBLE')
            os.system('pause')
    except ValueError:
        print('DATO INVALIDO')
        os.system('pause')
    else:
        return op
    
#########################################################################################################
    
    
def menu3():
    os.system('cls')
    titulo="""
    ++++++++++++++++++++++++++++++++++++++++
    +++++++++ FACTOR DE EMISION ++++++++++++
    ++++++++++++++++++++++++++++++++++++++++"""
    print(titulo)
    list=[1,2,3]
    options=['1. HIDRAULICA','2. TERMICA','3. RENOVABLE']
    for item in options:
        print(item)
    try:
        op=int(input('->'))
        if op not in list:
            print('OPCION NO DISPONIBLE')
            os.system('pause')
    except ValueError:
        print('DATO INVALIDO')
        os.system('pause')
    else:
        if op==1:
            fe=0
        elif op==2:
            fe=0.5
        else:
            fe=0.05
        os.system('cls')
        return fe
        

#########################################################################################################

def registro(dependencias:dict,dependencias_ver:dict):
    print('Esccriba una de las dependencias mostradas a continuacion: ')
    for key,value in dependencias.items():
        print (key)
    dependencia=input('->').upper()
    for key,value in dependencias.items():
        if dependencia == key:
            for key,value in dependencias[dependencia]['oficinas'].items():
                print (key)
            print('escriba una de las oficinas aqui mostradas')
            oficina=input('->').upper()
            for key,value in dependencias[dependencia]['oficinas'].items():
                if oficina==key:
                    op=menu1()
                    if op==1:
                        fe=menu3()
                        op2=menu2()
                        if op2==1:
                            consumoE=0
                            try:
                                ne=int(input('CUANTOS ELECTRODOMESTICOS DESEA INGRESAR: \n ->'))
                            except ValueError:
                                print('DATO INVALIDO, DEBEN SER NUMEROS ENTEROS')
                                os.system('pause')
                            else:
                                for i in range (ne):
                                    try:
                                        w=float(input(f'INGRESE LOS w DEL ELECTRODOMESTICO {i+1}: '))
                                        tiempoe=float(input(f'INGRESE EL TIEMPO EN HORAS DE CONSUMO DEL ELECTRODOMESTICO AL MES: '))
                                    except ValueError:
                                        print('DATO INVALIDO DEBEN SER NUMEROS')
                                        os.system('pause')
                                        break
                                    else:
                                        consumoE+=(w*tiempoe)/1000
                            c02_electro=consumoE*fe
                            dependencias[dependencia]['oficinas'][oficina]['electricidad']+= +c02_electro
                            dependencias_ver[dependencia]['electricidad']+=c02_electro
                            dependencias_ver[dependencia]['total']+=c02_electro

                        if op2==2:
                            consumoE=0
                            try:
                                kw=float(input('INGRESE LOS KW/H QUE RESGISTRA SU FACTURA: '))
                                tiempo=float(input(f'CANTIDAD DE MESES DE LA FACTURA. EJ SI ES BIMESTRAL INGRESE EL NUMERO 2: '))
                            except ValueError:
                                print('DATO INVALIDO, DEBEN SER NUMEROS')
                                os.system('pause')
                            else:
                                consumoE+=kw/tiempo
                            co2_recibo=consumoE*fe
                            dependencias[dependencia]['oficinas'][oficina]['electricidad']+= +co2_recibo
                            dependencias_ver[dependencia]['electricidad']+=co2_recibo
                            dependencias_ver[dependencia]['total']+=co2_recibo
                    if op==2:
                            fet=menu3()
                            consumoT=0
                            try:
                                km=float(input('INGRESE LOS km RECORRIDOS AL MES: '))
                            except ValueError:
                                print('DATO INVALIDO, DEBEN SER NUMEROS')
                                os.system('pause')
                            else:
                                consumoT+=km
                            co2_trans=consumoT*fet
                            dependencias[dependencia]['oficinas'][oficina]['transporte']+= +co2_trans
                            dependencias_ver[dependencia]['transporte']+=co2_trans
                            dependencias_ver[dependencia]['total']+=co2_trans







