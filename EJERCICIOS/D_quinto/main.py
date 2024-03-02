import modulos.menu as m
import modulos.addCity as ac
if __name__=='__main__':
    isRunning=True
    ciudadesYsismos=[]
    contador=int(0)
    while isRunning:
        op=m.menu1()
        if op==1:
            ac.ciudad(ciudadesYsismos)
        if op==2:
            while contador<1:
                n=int(input('numero de sismos por ciudad: '))
                contador=2

            ac.sismo(ciudadesYsismos,n)
        if op==3:
            ac.buscarSismos(ciudadesYsismos)
        if op==4:
            c=ac.comprobar(ciudadesYsismos)
            if c==True:
                for idx, item in enumerate(ciudadesYsismos):  
                    print(f'{idx+1}. {str(item[0]).upper()}')
                ciudad=int(input('seleccione la ciudad: '))
                promedio=ac.informes(ciudadesYsismos,ciudad)
                if promedio <2.5:
                    print(f'el promedio de los sismos es {promedio} y la {ciudad} esta en Amarillo, poco riesgo')
                    ac.os.system('pause')
                elif (promedio<4.5)and(promedio>=2.6):
                    print(f'el promedio de los sismos es {promedio} yla {ciudad} esta en Naranja, riesgo medio')
                    ac.os.system('pause')
                else:
                    print(f'el promedio de los sismos es {promedio} yla {ciudad} esta en rojo, riesgo alto')
                    ac.os.system('pause')
            if c==False:
                print('una o varias ciudades no tienen la misma cantidad de sismos')
                ac.os.system('pause')
            

        if op==5:
            isRunning=False
    pass 