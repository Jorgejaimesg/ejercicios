import os
def addDependenciasYOficinas(dependencias:dict,dependencias_ver:dict):
    
    nombre=input('ingrese el nombre de la dependencia: \n ->').upper()
    if nombre not in dependencias:
        try:
            n=int(input('cuantas oficinas posee esa dependencia: '))
        except ValueError:
            return
        dependencia={
            'nombre':nombre,
            'oficinas':{}
        }
        dependencia_ver={
            'nombre':nombre,
            'transporte':float(0),
            'electricidad':float(0),
            'total':float(0)
        }
        dependencias_ver[nombre]=dependencia_ver
        dependencias[nombre]=dependencia
        for i in range(n):
            oficina_nombre=input(f'ingrese el nombre de la oficina numero {i+1}: ').upper()
            oficina={
                'electricidad':0,
                'transporte':0
                }
            dependencias[nombre]['oficinas'][oficina_nombre]=oficina
        os.system('pause')
    else:
        print('LA DEPENDENCIA YA SE ENCUENTRA REGISTRADA')
        os.system('pause')