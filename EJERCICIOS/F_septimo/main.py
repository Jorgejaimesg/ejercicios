import modulos.menu as m
import modulos.addItem as i
import modulos.lista as L
import modulos.stock as s
import modulos.criticidad as c
import modulos.costos as g

if __name__=='__main__':
    inventario={}
    isRunning=True
    while isRunning:
        op=m.menuPrincipal()
        if op==1:
            isAddrunning=True
            while isAddrunning:
                i.add(inventario)
                isAddrunning=bool(input('DESEA INGRESAR OTRO PRODUCTO, S(SI) O ENTER(NO)'))
        if op==2:
            L.tabular(inventario)
            L.os.system('pause')
        if op==3:
            isstock=True
            while isstock:
                s.manipularStock(inventario)
                isstock=bool(input('DESEA INGRESAR O ELIMINAR OTRO PRODUCTO, S(SI) O ENTER(NO)'))
            s.os.system('pause')
        if op==4:
            c.crit(inventario)
            c.os.system('pause')
        if op==5:
            g.ganancias(inventario)
            g.ganancias_totales(inventario)
            g.os.system('pause')
        if op==6:
            isRunning=False


