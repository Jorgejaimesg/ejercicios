import os
def addPlayer(torneo:dict):
    id=input('INGRESE EL ID DEL JUGADOR: ').upper()
    if (id not in torneo['novato']) and (id not in torneo['intermedio']) and (id not in torneo['avanzado']):
        nombre=input('INGRESE EL NOMBRE DEL PARTICIPANTE: ').upper()
        try:
            edad=int(input('INGRESE LA EDAD DEL COMPETIDOR: '))
            if edad <0:
                print('NO SE PUEDEN TENER EDADES NEGATIVAS')
        except ValueError:
            print('DATO INVALIDO')
        else:
            jugador={
                'id':id,
                'nombre':nombre,
                'PJ':0,
                'PG':0,
                'PP':0,
                'PA':0,
                'TP':0
            }
            
            if edad>=15 and edad<=16:
                torneo['novato'][id]=jugador
                print (F'PARTICIPANTE CON {id} Y NOMBRE {nombre} REGISTRADO EN NOVATOS')
            elif edad>=17 and edad<=20:
                torneo['intermedio'][id]=jugador
                print (F'PARTICIPANTE CON {id} Y NOMBRE {nombre} REGISTRADO EN INTERMEDIOS')
            elif edad>20:
                torneo['avanzado'][id]=jugador
                print (F'PARTICIPANTE CON {id} Y NOMBRE {nombre} REGISTRADO EN AVANZADOS')
            else:
                print ('MUY JOVEN PARA PARTICIPAR')
    else:
        print('YA ESTA REGISTRADO')
               
        
