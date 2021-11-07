
import random

def multiplicacion(valores):
    resultado=[1]
    for valor in range(0,len(valores)):
        resultado[0]=resultado[0]*valores[valor]
    return resultado[0]
    
def suma(valores):
    resultado=[0]
    for valor in range(0,len(valores)):
        resultado[0]=resultado[0]+valores[valor]
    return resultado[0]


def resta(valores):
    resultado=[valores[0]]
    for valor in range(0,len(valores)-1):
        if valor==0:
            resultado[0]=resultado[0]-valores[1]
        else:
            resultado[0]=resultado[0]-valores[valor]
     
    return resultado[0]

def division(valores):
    resultado=[1]
    for valor in range(0,len(valores)):
        resultado[0]=resultado[0]/valores[valor]
    return resultado[0]

you=input("tu quieres dar el ejercicio?")

if you=="si" or you=="yes":
    exer=input("ejercicio:\n")

    values=[0]
    values_two=[0]
    baselist=[0]
    baselist_two=[0]
    rpoten=[]
    rpoten_two=[]
    x=0
    x2=0

    if "*" in exer:
        divop=exer.split("*")
        operation="*"

    elif "-" in exer:
        divop=exer.split("-")
        operation="-"

    elif "+" in exer:
        divop=exer.split("+")
        operation="+"

    elif "/" in exer:
        divop=exer.split("/")
        operation="/"

    if "V" in exer:
        
        divexer=divop[0].split("V")
        divexer[1]=divexer[1].split(",")
        divexer_two=divop[1].split("V")
        divexer_two[1]=divexer_two[1].split(",")
        base=int(divexer[0])
        number=int(divexer[1][0])
        potentia=int(divexer[1][1])
        base_two=int(divexer_two[0])
        number_two=int(divexer_two[1][0])
        potentia_two=int(divexer_two[1][1])

    elif "v" in exer:
    
        divexer=divop[0].split("v")
        divexer[1]=divexer[1].split(",")
        divexer_two=divop[1].split("v")
        divexer_two[1]=divexer_two[1].split(",")
        base=int(divexer[0])
        number=int(divexer[1][0])
        potentia=int(divexer[1][1])
        base_two=int(divexer_two[0])
        number_two=int(divexer_two[1][0])
        potentia_two=int(divexer_two[1][1])


    while x<potentia:
        rpoten.append(str(number))
        x=x+1
    while x2<potentia_two:
        rpoten_two.append(str(number_two))
        x2=x2+1


    if operation=='*':
        
        values[0]=number**potentia
        baselist[0]=multiplicacion([base,values[0]])
        values_two[0]=number_two**potentia_two
        baselist_two[0]=multiplicacion([base_two,values_two[0]])
        producto=multiplicacion([baselist[0],baselist_two[0]])

    elif operation=='+':
        values[0]=number**potentia
        baselist[0]=multiplicacion([base,values[0]])
        values_two[0]=number_two**potentia_two
        baselist_two[0]=multiplicacion([base_two,values_two[0]])
        producto=suma([baselist[0],baselist_two[0]])
    
    elif operation=='-':
        values[0]=number**potentia
        baselist[0]=multiplicacion([base,values[0]])
        values_two[0]=number_two**potentia_two
        baselist_two[0]=multiplicacion([base_two,values_two[0]])
        producto=resta([baselist[0],baselist_two[0]])
        
    
    elif operation=='/':
        values[0]=number**potentia
        baselist[0]=multiplicacion([base,values[0]])
        values_two[0]=number_two**potentia_two
        baselist_two[0]=multiplicacion([base_two,values_two[0]])
        producto=division([baselist[0],baselist_two[0]])
            
    print('\n%sV%s,%s %s %sV%s,%s =\n\n%s(%s) %s %s(%s)\n%s(%s) %s %s(%s) \n%s %s %s\n%s\n' % (str(base),str(number),str(potentia),str(operation),str(base_two),str(number_two),str(potentia_two),str(base),'*'.join(rpoten),str(operation),str(base_two),'*'.join(rpoten_two),str(base),str(values[0]),str(operation),str(base_two),str(values_two[0]),str(baselist[0]),str(operation),str(baselist_two[0]),str(producto)))

else:

    cant=input('cuantos ejercicios?\n')
    cant=int(cant)
    operation=input('operación: \n')

    for n in range(0,cant):

        base=random.randint(1,9)
        base_two=random.randint(1,9)
        number=random.randint(2,9)
        number_two=random.randint(2,9)
        potentia=random.randint(2,9)
        potentia_two=random.randint(2,9)

        values=[0]
        values_two=[0]
        baselist=[0]
        baselist_two=[0]
        rpoten=[]
        rpoten_two=[]
        x=0
        x2=0
        while x<potentia:
            rpoten.append(str(number))
            x=x+1
        while x2<potentia_two:
            rpoten_two.append(str(number_two))
            x2=x2+1

        if operation=="all":
            pastop="all"
            if n==0:
                exdiv=input("quieres divisiones?")
            if exdiv=="si":
                opnum=random.randint(1,4)
            
            else:
                opnum=random.randint(1,3)

            if opnum==1:
                operation="+"

            elif opnum==2:
                operation="-"

            elif opnum==3:
                operation="*"

            elif opnum==4:
                operation="/"


        if operation=='*':
            
            values[0]=number**potentia
            baselist[0]=multiplicacion([base,values[0]])
            values_two[0]=number_two**potentia_two
            baselist_two[0]=multiplicacion([base_two,values_two[0]])
            producto=multiplicacion([baselist[0],baselist_two[0]])

        elif operation=='+':
            values[0]=number**potentia
            baselist[0]=multiplicacion([base,values[0]])
            values_two[0]=number_two**potentia_two
            baselist_two[0]=multiplicacion([base_two,values_two[0]])
            producto=suma([baselist[0],baselist_two[0]])
        
        elif operation=='-':
            values[0]=number**potentia
            baselist[0]=multiplicacion([base,values[0]])
            values_two[0]=number_two**potentia_two
            baselist_two[0]=multiplicacion([base_two,values_two[0]])
            producto=resta([baselist[0],baselist_two[0]])
            
        
        elif operation=='/':
            values[0]=number**potentia
            baselist[0]=multiplicacion([base,values[0]])
            values_two[0]=number_two**potentia_two
            baselist_two[0]=multiplicacion([base_two,values_two[0]])
            producto=division([baselist[0],baselist_two[0]])
                
        print('%sV%s,%s %s %sV%s,%s =\n\n%s(%s) %s %s(%s)\n%s(%s) %s %s(%s) \n%s %s %s\n%s\n' % (str(base),str(number),str(potentia),str(operation),str(base_two),str(number_two),str(potentia_two),str(base),'*'.join(rpoten),str(operation),str(base_two),'*'.join(rpoten_two),str(base),str(values[0]),str(operation),str(base_two),str(values_two[0]),str(baselist[0]),str(operation),str(baselist_two[0]),str(producto)))

    # al poner if pastop=="all" en el try, lo hará. si sale error, este no aparecerá en la consola
        try:
            if pastop=="all":
                operation="all"
        except NameError:
            break
