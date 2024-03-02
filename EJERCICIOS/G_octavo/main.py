import modulos.menu as m
import modulos.addParticipante as add
import modulos.ver as v
import modulos.ingresarpartido as p
import modulos.max as max
if __name__ =='__main__':
    torneo={
        'novato':{},
        'intermedio':{},
        'avanzado':{}
    }
    isRunning=True
    while isRunning:
        m.os.system('cls')
        op=m.menuP()
        if op==1:
            isadd=True
            while isadd:
                add.addPlayer(torneo)
                isadd=bool(input('DESEA INGRESAR OTRO JUGADOR S(SI) O ENTER(NO)'))
                m.os.system('cls')
        if op==2:
            v.lista(torneo)
        if op==3:
            isfecha=True
            while isfecha:
                p.addMatch(torneo)
                isfecha=bool(input('DESEA INGRESAR OTRO PARTIDO S(SI) O ENTER(NO)'))
                m.os.system('cls')
        if op==4:
            max.reportes(torneo)
        if op==5:
            isRunning=False
    