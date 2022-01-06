import random
import re

# e.g. 3p3 + 1p1
re_ejercicio = re.compile(r"""\s* #verifica si hay algun espacio antes del primer número
                            (\d+) #estos son los números antes de la P
                            \s*
                          [Pp]{1} #esta es la P
                          \s* #espacios después de la primera P
                          (\d+) #este es el digito despues de la primera P
                          \s* #espacios antes del signo
                          ([-+*/]){1} #este es el signo que indica la operación a realizar
                           \s* #espacios despues del signo y antes del tercer número
                          (\d+) #este es el digito antes de la segunda P
                           \s* #los espacios que hay antes de la segunda P
                           [Pp]{1} #esta es la segunda P  
                           \s* #espacios antes del cuarto número
                          (\d+) #este es el número despues de la segunda P
                          \s*"""
                          
                           , re.VERBOSE)

# funciones


def permutaciones(numero_a_permutar):
    # ??? aquí se guardarán los numeros de la permutacion.
    # e.g. permutacion de 3 = 3 x 2 x 1
    numeros_permutacion = [] 
    resultado_permutacion = 1
    for numero in range(numero_a_permutar, 0, -1):
        numeros_permutacion.append(numero)
        resultado_permutacion *= numero
    return [numeros_permutacion, resultado_permutacion]

# clases de excepciones para las funciones
class NotAPermutation(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

class NoSuchOperation(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        




        
# toma como primer parámetro el signo de una operación aritmetica básica y como segundo
# un array, al que se le va a realizar la operacion
def realizar_operacion(operacion, valores):

# multiplicar todos los elementos de un array
    if operacion == '*':
        valor_inicial = valores[0]
        for valor in valores[1:]:
            valor_inicial *= valor 


# restar todos los elementos de un array
    elif operacion == '-':
        valor_inicial = valores[0]
        for valor in valores[1:]:
            valor_inicial -= valor 

# dividir todos los elementos de un array
    elif operacion == '/':
        valor_inicial = valores[0]
        for valor in valores[1:]:
            valor_inicial /= valor 

# sumar todos los elementos de un array
    elif operacion == '+':
        valor_inicial = valores[0]
        for valor in valores[1:]:
            valor_inicial += valor 

# si el primer argumento posicional no es uno de los signos que pueden ser elegidos,
# lanza una excepcion y detiene el programa
    else:
        raise NoSuchOperation(f'La operación ( {operacion} ) no existe.  ')

    return valor_inicial
# error
        

    

# ??? quien ejecuta el script decide si la computadora crea el ejercicio o si lo da el usuario
you = input("tu quieres dar el ejercicio?\n(Y|S|s|N)\n")


if you=='Y' or you == 'y' or you == 's' or you == 'S':
    exer=input("ejercicio:\n")
    valores_a_permutar =  re_ejercicio.findall(exer) 
    if valores_a_permutar == []:
        raise NotAPermutation('LO INSERTADO EN EL INPUT NO ES UNA PERMUTACIÓN.')
    valores_a_permutar = list(valores_a_permutar[0])


    # número antes de la primera p, por el que se multiplicará el resultado de esa permutación
    base = int(valores_a_permutar[0])
    # el primer número a permutar
    number=int(valores_a_permutar[1])
    # la operacion a realizar
    operation = valores_a_permutar[2]
    # número antes de la primera p, por el que se multiplicará el resultado de esa permutación
    base_two=int(valores_a_permutar[3])
    # el segundo número a permutar
    number_two=int(valores_a_permutar[4])
    

    # if "*" in exer:
        # divop=exer.split("*")
        # operation="*"

    # elif "-" in exer:
        # divop=exer.split("-")
        # operation="-"

    # elif "+" in exer:
        # divop=exer.split("+")
        # operation="+"

    # elif "/" in exer:
        # divop=exer.split("/")
        # operation="/"

    # if "P" in exer:
        
        # divexer=divop[0].split("P")
        # divexer_two=divop[1].split("P")
        # base=int(divexer[0])
        # number=int(divexer[1])
        # base_two=int(divexer_two[0])
        # number_two=int(divexer_two[1])
    

    # elif "p" in exer:
        # divexer=divop[0].split("p")
        # divexer_two=divop[1].split("p")
        # base=int(divexer[0])
        # number=int(divexer[1])
        # base_two=int(divexer_two[0])
        # number_two=int(divexer_two[1])
    

        
    # permutacion de los números despues de las P's
    permutacion_primer_numero = permutaciones(number)
    permutacion_segundo_numero = permutaciones(number_two)
    
    permutacion_por_base1 = base * permutacion_primer_numero[1]
    permutacion_por_base2= base_two * permutacion_segundo_numero[1]

    resultado = realizar_operacion(operation, [permutacion_por_base1, permutacion_por_base2])

    # if operation=='*':
        # operation = 'multiplicacion'

        
        # values[0]=multiplicacion(permutation)
        # baselist[0]=multiplicacion([base,values[0]])
        # values_two[0]=multiplicacion(permutation_two)
        # producto=multiplicacion([baselist[0],baselist_two[0]])


    # elif operation=='+':
        # operation = 'suma'
        
#         values[0]=multiplicacion(permutation)
        # baselist[0]=multiplicacion([base,values[0]])
        # values_two[0]=multiplicacion(permutation_two)
        # baselist_two[0]=multiplicacion([base_two,values_two[0]])
        # producto=suma([baselist[0],baselist_two[0]])
    

    # elif operation=='-':
        # operation = 'resta'
        
        # values[0]=multiplicacion(permutation)
        # baselist[0]=multiplicacion([base,values[0]])
        # values_two[0]=multiplicacion(permutation_two)
        # baselist_two[0]=multiplicacion([base_two,values_two[0]])
        # producto=resta([baselist[0],baselist_two[0]])

    
    # elif operation=='/':
        # operation = 'division'
        
        # values[0]=multiplicacion(permutation)
        # baselist[0]=multiplicacion([base,values[0]])
        # values_two[0]=multiplicacion(permutation_two)
        # baselist_two[0]=multiplicacion([base_two,values_two[0]])
        # producto=division([baselist[0],baselist_two[0]])

    # uso esto para evitar escribir la misma mrd un montón de veces como antes
    # esto ejecutará la funcion correspondiente 
    
    
    permutacion_primer_numero[0] = '*'.join([str(numero) for numero in permutacion_primer_numero[0]])
    permutacion_segundo_numero[0] = '*'.join([str(numero) for numero in permutacion_segundo_numero[0]])



    print(
f'''{base}P{number} {operation} {base_two}P{number_two} =
{base}({permutacion_primer_numero[0]}) {operation} {base_two}({permutacion_segundo_numero[0]})
{base}({permutacion_primer_numero[1]}) {operation} {base_two}({permutacion_segundo_numero[1]})
{permutacion_por_base1} {operation} {permutacion_por_base2}
{resultado}\n\n''')


else:
    cant=input('¿Cuantos ejercicios quieres?\n')
    cant=int(cant)
    operation=input('Elige una operación para los ejercicios:\n(+), (-), (*), (/), (ALL)\n')

    for n in range(cant):

        if operation == "ALL":
            operation = random.choice(['-', '*', '+', '/'])

        base=random.randint(1,9)
        base_two=random.randint(1,9)
        number=random.randint(1,9)
        number_two=random.randint(1,9)

        permutacion_primer_numero = permutaciones(number)
        permutacion_segundo_numero = permutaciones(number_two)
        
        permutacion_por_base1 = base * permutacion_primer_numero[1]
        permutacion_por_base2= base_two * permutacion_segundo_numero[1]

        

        resultado = realizar_operacion(operation, [permutacion_por_base1, permutacion_por_base2])

        # values=[0]
        # values_two=[0]
        # baselist=[0]
        # baselist_two=[0]
        # permutation=[]
        # permutation_two=[]

        # while number>0:
            # permutation.append(number)
            # number=number-1
            
        # while number_two>0:
            # permutation_two.append(number_two)
            # number_two=number_two-1



        # if operation=='*':
            
            # values[0]=multiplicacion(permutation)
            # baselist[0]=multiplicacion([base,values[0]])
            # values_two[0]=multiplicacion(permutation_two)
            # baselist_two[0]=multiplicacion([base_two,values_two[0]])
            # producto=multiplicacion([baselist[0],baselist_two[0]])


        # elif operation=='+':
            
            # values[0]=multiplicacion(permutation)
            # baselist[0]=multiplicacion([base,values[0]])
            # values_two[0]=multiplicacion(permutation_two)
            # baselist_two[0]=multiplicacion([base_two,values_two[0]])
            # producto=suma([baselist[0],baselist_two[0]])
        

        # elif operation=='-':
            
            # values[0]=multiplicacion(permutation)
            # baselist[0]=multiplicacion([base,values[0]])
            # values_two[0]=multiplicacion(permutation_two)
            # baselist_two[0]=multiplicacion([base_two,values_two[0]])
            # producto=resta([baselist[0],baselist_two[0]])

        
        # elif operation=='/':
            
            # values[0]=multiplicacion(permutation)
            # baselist[0]=multiplicacion([base,values[0]])
            # values_two[0]=multiplicacion(permutation_two)
            # baselist_two[0]=multiplicacion([base_two,values_two[0]])
            # producto=division([baselist[0],baselist_two[0]])

        
        # for w in range(0,len(permutation)):
            # permutation[w]=str(permutation[w])

        # for w in range(0,len(permutation_two)):
            # permutation_two[w]=str(permutation_two[w])

        permutacion_primer_numero[0] = '*'.join([str(numero) for numero in permutacion_primer_numero[0]])
        permutacion_segundo_numero[0] = '*'.join([str(numero) for numero in permutacion_segundo_numero[0]])


        print(
f'''{base}P{number} {operation} {base_two}P{number_two} =
{base}({permutacion_primer_numero[0]}) {operation} {base_two}({permutacion_segundo_numero[0]})
{base}({permutacion_primer_numero[1]}) {operation} {base_two}({permutacion_segundo_numero[1]})
{permutacion_por_base1} {operation} {permutacion_por_base2}
{resultado}\n\n''')


            # print('''\n%sP%s %s %sP%s =
                
    # %s(%s) %s %s(%s)
    # %s(%s) %s %s(%s)
    # %s %s %s\n%s\n''' %(str(base),str(permutation[0]),operation,str(base_two),str(permutation_two[0]),str(base),'*'.join(permutation),str(operation), str(base_two),'*'.join(permutation_two),str(base),str(values[0]),str(operation),str(base_two),str(values_two[0]),str(baselist[0]),str(operation),str(baselist_two[0]),str(producto)))

            # try:
                # if pastop=="all":
                    # operation="all"
            # except NameError:
                # break
