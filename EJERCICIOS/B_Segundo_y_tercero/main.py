
import modulos.menu as m
import modulos.addStudent as s
import modulos.verEstudiantes as l
import modulos.menu2 as m2
import modulos.buscar as b
if __name__=='__main__':
    students={}
    isapprunning=True
    while isapprunning==True:
        op=m.menu()
        if op==1:
            s.newStudent(students)
        if op==2:
            l.list(students)
        if op==3:
            isReports=True
            while isReports==True:
                opr=m2.menu2()
                if opr=='A': ##PESO IDEAL
                    max=b.bucarCategoria(students,'normal')
                    print(f'EL TOTAL DE PERSONAS CON PESO IDEAL ES: {max} ')
                if opr=='B': ## OBESIDAD GRADO I
                    max=b.bucarCategoria(students,'obesidad 1')
                    print(f'EL TOTAL DE PERSONAS CON OBESIDAD GRADO I ES: {max} ')
                if opr=='C': ## OBESIDAD GRADO II
                    max=b.bucarCategoria(students,'obesidad 2')
                    print(f'EL TOTAL DE PERSONAS CON OBESIDAD GRADO II ES: {max} ')
                if opr=='D': ## OBESIDAD GRADO III
                    max=b.bucarCategoria(students,'obesidad 3')
                    print(f'EL TOTAL DE PERSONAS CON OBESIDAD GRADO III ES: {max} ')
                if opr=='E':## SOBREPESP
                    max=b.bucarCategoria(students,'sobrepeso')
                    print(f'EL TOTAL DE PERSONAS CON SOBREPESO ES: {max} ')
                if opr=='F':
                    isReports=False
        if op==4:
            isapprunning=False