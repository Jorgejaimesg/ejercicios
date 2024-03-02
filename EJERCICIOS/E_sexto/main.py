import modulos.menu as m
import modulos.addDependencia as ad
import modulos.registroConsumo as r
import modulos.ver as v
import modulos.sumas as s

if __name__ == '__main__':
    dependencias={}
    dependencias_ver={}
    isRunning=True
    while isRunning:
        op=m.menuP()
        if op==1:
            ad.addDependenciasYOficinas(dependencias,dependencias_ver)
        if op==2:
            v.lista(dependencias_ver)
            v.os.system('pause')
        if op==3:
            r.registro(dependencias,dependencias_ver)
            print(dependencias)
        if op==4:
            s.totalco2(dependencias_ver)
            s.os.system('pause')
        if op==5:
            s.mayorco2(dependencias_ver)
            s.os.system('pause')
        if op==6:
            isRunning=False