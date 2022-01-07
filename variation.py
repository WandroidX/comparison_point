import random
import re
import os

# e.g. 3p3 + 1p1
re_ejercicio = re.compile(r"""\s* #verifica si hay algun espacio antes del primer número
                            (\d+) #esta es la base de la primera variación
                            \s*
                          [Vv]{1} #esta es la V
                          \s* #espacios después de la primera V
                          (\d+) #este es el digito antes de la primera coma
                          \s* #espacios antes de la coma
                          , #una coma para separar el numero potenciado del potenciador
                          \s* #espacios después de la coma
                          (\d+) #este es el digito despues de la primera coma
                          \s* #espacios antes del signo

                          ([-+*/]){1} #este es el signo que indica la operación a realizar

                        \s* #verifica si hay algun espacio después del signo
                            (\d+) #esta es la base de la segunda variacion
                            \s*
                          [Vv]{1} #esta es la V
                          \s* #espacios después de la primera V
                          (\d+) #este es el digito antes de la primera coma
                          \s* #espacios antes de la coma
                          , #una coma para separar el numero potenciado del potenciador
                          \s* #espacios después de la coma
                          (\d+) #este es el digito despues de la primera coma
                          \s* #espacios al final del ejercicio""", re.VERBOSE)


# e.g. 3V2,2 + 1V2,3
def variaciones(potenciado, potenciador):
    potencia_detallada = []
    for numero in range(potenciador):
        potencia_detallada.append( potenciado )

    return [potencia_detallada, potenciado ** potenciador]

# clases de excepciones para las funciones
class NotAVariation(Exception):
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
    valores_a_variar =  re_ejercicio.findall(exer) 
    if valores_a_variar == []:
        raise NotAVariation('LO INSERTADO EN EL INPUT NO ES UNA VARIACIÓN.')
    valores_a_variar = list(valores_a_variar[0])


    # número antes de la primera p, por el que se multiplicará el resultado de esa variación
    base = int(valores_a_variar[0])
    # el primer número a variar
    potenciado=int(valores_a_variar[1])
    potenciador = int(valores_a_variar[2])

    # la operacion a realizar
    operation = valores_a_variar[3]

    # número antes de la primera p, por el que se multiplicará el resultado de esa variación

    base_two=int(valores_a_variar[4])
    # el segundo número a variar
    potenciado_two =int(valores_a_variar[5])
    potenciador_two = int(valores_a_variar[6])

    # ??? estas son las variaciones de los números en el ejercicio
    variacion_primer_numero = variaciones(potenciado, potenciador)
    variacion_segundo_numero = variaciones(potenciado_two, potenciador_two)

    # ??? este es el resultado de multiplicar el resultado de las variaciones de los 
    # numeros (los que están después de la P) por las bases (los que están antes de la P)
    variacion_por_base1 = base * variacion_primer_numero[1]
    variacion_por_base2= base_two * variacion_segundo_numero[1]

    # ??? este el el resultado final del ejercicio
    resultado = realizar_operacion(operation, [variacion_por_base1, variacion_por_base2])
    
    # ??? convierte los numeros del primer array arrojado por la funcion variacion
    # en strings para luego junarlos con join usando como separador signo de multiplicacion
    variacion_primer_numero[0] = '*'.join([str(numero) for numero in variacion_primer_numero[0]])
    variacion_segundo_numero[0] = '*'.join([str(numero) for numero in variacion_segundo_numero[0]])

    os.system('cls')

    print(
f'''{base}V{potenciado},{potenciador} {operation} {base_two}V{potenciado_two},{potenciador_two} =
{base}({variacion_primer_numero[0]}) {operation} {base_two}({variacion_segundo_numero[0]})
{base}({variacion_primer_numero[1]}) {operation} {base_two}({variacion_segundo_numero[1]})
{variacion_por_base1} {operation} {variacion_por_base2}
{resultado}\n\n''')


else:
    cant=input('¿Cuantos ejercicios quieres?\n')
    cant=int(cant)
    operation=input('Elige una operación para los ejercicios:\n(+), (-), (*), (/), (ALL)\n')

    for n in range(cant):

        # ??? si el usuario escribe ALL en el input de operation, 
        # se escoge una operación al azar
        if operation == "ALL" or operation == 'all':
            operation = random.choice(['-', '*', '+', '/'])
            todas_operaciones = True

        # ??? se generan bases y números aleatorios para conformar 
        # el ejercicio
        base = random.randint(1,9)
        # el primer número a variar
        potenciado=random.randint(1,9)
        potenciador = random.randint(1,9)


        # número antes de la primera p, por el que se multiplicará el resultado de esa variación

        base_two=random.randint(1,9)
        # el segundo número a variar
        potenciado_two =random.randint(1,9)
        potenciador_two =random.randint(1,9)

        # ??? estas son las variaciones de los números en el ejercicio
        variacion_primer_numero = variaciones(potenciado, potenciador)
        variacion_segundo_numero = variaciones(potenciado_two, potenciador_two)

        # ??? este es el resultado de multiplicar el resultado de las variaciones de los 
        # numeros (los que están después de la P) por las bases (los que están antes de la P)
        variacion_por_base1 = base * variacion_primer_numero[1]
        variacion_por_base2= base_two * variacion_segundo_numero[1]

        # ??? este el el resultado final del ejercicio
        resultado = realizar_operacion(operation, [variacion_por_base1, variacion_por_base2])
        
        # ??? convierte los numeros del primer array arrojado por la funcion variacion
        # en strings para luego junarlos con join usando como separador signo de multiplicacion
        variacion_primer_numero[0] = '*'.join([str(numero) for numero in variacion_primer_numero[0]])
        variacion_segundo_numero[0] = '*'.join([str(numero) for numero in variacion_segundo_numero[0]])


        if n == 0:
            os.system('cls')
        print(
    f'''{base}V{potenciado},{potenciador} {operation} {base_two}V{potenciado_two},{potenciador_two} =
    {base}({variacion_primer_numero[0]}) {operation} {base_two}({variacion_segundo_numero[0]})
    {base}({variacion_primer_numero[1]}) {operation} {base_two}({variacion_segundo_numero[1]})
    {variacion_por_base1} {operation} {variacion_por_base2}
    {resultado}\n\n''')

        if todas_operaciones == True:
            operation = 'ALL'

