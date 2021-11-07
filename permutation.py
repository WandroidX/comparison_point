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
    permutation=[]
    permutation_two=[]

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

    if "P" in exer:
        
        divexer=divop[0].split("P")
        divexer_two=divop[1].split("P")
        base=int(divexer[0])
        number=int(divexer[1])
        base_two=int(divexer_two[0])
        number_two=int(divexer_two[1])
    

    elif "p" in exer:
        divexer=divop[0].split("p")
        divexer_two=divop[1].split("p")
        base=int(divexer[0])
        number=int(divexer[1])
        base_two=int(divexer_two[0])
        number_two=int(divexer_two[1])
    

        
    while number>0:
        permutation.append(number)
        number=number-1
        
    while number_two>0:
        permutation_two.append(number_two)
        number_two=number_two-1

    if operation=='*':
        
        values[0]=multiplicacion(permutation)
        baselist[0]=multiplicacion([base,values[0]])
        values_two[0]=multiplicacion(permutation_two)
        baselist_two[0]=multiplicacion([base_two,values_two[0]])
        producto=multiplicacion([baselist[0],baselist_two[0]])


    elif operation=='+':
        
        values[0]=multiplicacion(permutation)
        baselist[0]=multiplicacion([base,values[0]])
        values_two[0]=multiplicacion(permutation_two)
        baselist_two[0]=multiplicacion([base_two,values_two[0]])
        producto=suma([baselist[0],baselist_two[0]])
    

    elif operation=='-':
        
        values[0]=multiplicacion(permutation)
        baselist[0]=multiplicacion([base,values[0]])
        values_two[0]=multiplicacion(permutation_two)
        baselist_two[0]=multiplicacion([base_two,values_two[0]])
        producto=resta([baselist[0],baselist_two[0]])

    
    elif operation=='/':
        
        values[0]=multiplicacion(permutation)
        baselist[0]=multiplicacion([base,values[0]])
        values_two[0]=multiplicacion(permutation_two)
        baselist_two[0]=multiplicacion([base_two,values_two[0]])
        producto=division([baselist[0],baselist_two[0]])

    
    for w in range(0,len(permutation)):
        permutation[w]=str(permutation[w])

    for w in range(0,len(permutation_two)):
        permutation_two[w]=str(permutation_two[w])

    print('\n%sP%s %s %sP%s =\n\n%s(%s) %s %s(%s)\n%s(%s) %s %s(%s)\n%s %s %s\n%s\n' %(str(base),str(permutation[0]),operation,str(base_two),str(permutation_two[0]),str(base),'*'.join(permutation),str(operation), str(base_two),'*'.join(permutation_two),str(base),str(values[0]),str(operation),str(base_two),str(values_two[0]),str(baselist[0]),str(operation),str(baselist_two[0]),str(producto)))


else:
    cant=input('cuantos ejercicios?\n')
    cant=int(cant)
    operation=input('operación: \n')

    for n in range(0,cant):

        base=random.randint(1,9)
        base_two=random.randint(1,9)
        number=random.randint(2,9)
        number_two=random.randint(2,9)

        values=[0]
        values_two=[0]
        baselist=[0]
        baselist_two=[0]
        permutation=[]
        permutation_two=[]

        while number>0:
            permutation.append(number)
            number=number-1
            
        while number_two>0:
            permutation_two.append(number_two)
            number_two=number_two-1

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
            
            values[0]=multiplicacion(permutation)
            baselist[0]=multiplicacion([base,values[0]])
            values_two[0]=multiplicacion(permutation_two)
            baselist_two[0]=multiplicacion([base_two,values_two[0]])
            producto=multiplicacion([baselist[0],baselist_two[0]])


        elif operation=='+':
            
            values[0]=multiplicacion(permutation)
            baselist[0]=multiplicacion([base,values[0]])
            values_two[0]=multiplicacion(permutation_two)
            baselist_two[0]=multiplicacion([base_two,values_two[0]])
            producto=suma([baselist[0],baselist_two[0]])
        

        elif operation=='-':
            
            values[0]=multiplicacion(permutation)
            baselist[0]=multiplicacion([base,values[0]])
            values_two[0]=multiplicacion(permutation_two)
            baselist_two[0]=multiplicacion([base_two,values_two[0]])
            producto=resta([baselist[0],baselist_two[0]])

        
        elif operation=='/':
            
            values[0]=multiplicacion(permutation)
            baselist[0]=multiplicacion([base,values[0]])
            values_two[0]=multiplicacion(permutation_two)
            baselist_two[0]=multiplicacion([base_two,values_two[0]])
            producto=division([baselist[0],baselist_two[0]])

        
        for w in range(0,len(permutation)):
            permutation[w]=str(permutation[w])

        for w in range(0,len(permutation_two)):
            permutation_two[w]=str(permutation_two[w])

        print('\n%sP%s %s %sP%s =\n\n%s(%s) %s %s(%s)\n%s(%s) %s %s(%s)\n%s %s %s\n%s\n' %(str(base),str(permutation[0]),operation,str(base_two),str(permutation_two[0]),str(base),'*'.join(permutation),str(operation), str(base_two),'*'.join(permutation_two),str(base),str(values[0]),str(operation),str(base_two),str(values_two[0]),str(baselist[0]),str(operation),str(baselist_two[0]),str(producto)))

        try:
            if pastop=="all":
                operation="all"
        except NameError:
            break
