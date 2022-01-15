import re, sys, logging
archivo = sys.argv[1]




re_espacio = re.compile(r'\S')
re_igual = re.compile(r'=')
re_coma = re.compile(r',')
re_slash = re.compile(r'/')

re_operadores = re.compile(r'[-!+*/=<>]{1}')
def sustituir_en_str(inicio, fin, string_where, string_for):
    # convierte en lista el string_where, sustituye
    # por espacios en blanco todo en la lista entre inicio
    # y fin y lo cambia por string_for
    lista = list(string_where)
    lista[inicio: fin] = ''
    lista.insert(inicio, string_for)
    return ''.join(lista)

# ??? FUNCTION_INFO: retorna el string argumento pero sin sus espacios iniciales
# y tambien la cantidad de estos espacios (util para regresar esos espacios mas adelante)
def guardar_indentacion(string_where):
    contador_espacios = 0
    while string_where.startswith(' '):
        string_where = list(string_where)
        string_where[0] = ''
        contador_espacios += 1
        # importante: como el while cada vez divide string_where,
        # al final del mismo debe unirse de nuevo para evitar errores
        string_where = ''.join( string_where ) 

    return [string_where, contador_espacios]


# ??? FUNCTION_INFO: retorna el string dado como argumento pero con los espacios dobles
# convertidos en solo uno (excepto si el espacio doble está dentro de un par de comillas)

def quitar_espacio_doble(string_where):
    re_string = re.compile(r'''
\'\'\'.*?\'\'\'| # triples comillas simples y todo lo que esté dentro (non-greedy)
""".*?"""| # triples comillas dobles y todo lo que esté dentro de ellas (non-greedy)
\'.*?\'| # comillas simples y todo lo que esté dentro de ellas (non-greedy)
\".*?\" #comillas dobles y todo lo que esté dentro de ellas (non-greedy)
''',
re.VERBOSE)

    # aqui estarán las ubicaciones de los pares de comillas en el string
    # where
    ubicacion_comillas = [[comillas.start(), comillas.end() - 1] for comillas in re_string.finditer(string_where)]


    
    lista_caracteres = list(string_where)
    
    for indice, caracter in enumerate( lista_caracteres ):
        # si el caracter actual es un espacio, intentará saber si el que le sigue tambien
        # es un espacio
        if caracter == ' ':

            try:
                if lista_caracteres[indice + 1] == ' ':
                    if ubicacion_comillas:
                        # en inicio y fin se guarda donde empiezan
                        # y terminan los pares de comillas 
                        for inicio, fin in ubicacion_comillas:
                            
                            # si el indice del caracter actual es mayor que el inicio del par
                            # de comillas actuales y tambien es menor que el fin del mismo
                            # par de comillas, significa que el espacio doble está dentro
                            # de comillas y por lo tanto no se sustituye el espacio
                            if indice > inicio:
                                if indice  < fin:
                                    break
                                # si el indice es mayor al inicio, pero menor al fin de las
                                # comillas, convierte el caracter indice en nada('  ')
                                elif indice > fin:
                                    lista_caracteres[indice] = ''
                            # si el indice es menor al inicio de las
                            # comillas, convierte el caracter actual en nada('')
                            elif indice < inicio:
                                lista_caracteres[indice] = ''
                    # si ubicacion comillas está vacio, entonces el caracter actual
                    # se convierte en nada ('')
                    elif not ubicacion_comillas:
                        lista_caracteres[indice] = ''

            # si da error de indice (si el caracter actual es el ultimo caracter),
            # break
            except IndexError:
                break

    # ahora string_where es la lista de caracteres modificada con los espacios dobles
    # quitados
    string_where = ''.join( lista_caracteres )

    return string_where
            




# añade un espacio antes y despues de la ubicacion de todas las 
# coincidencias de regex
# toma como parametros una lista de strings, la expresion regular a buscar 
# en esos strings y una excepcion que impedira que se añada el espacio
# antes o despues
def añadir_espacios(list_string_where, re_target, re_excepciones = None, despues = True, antes = True ):

    # la funcion lanza una excepcion si el primer argumento posicional
    # no es una lista
    assert antes or despues, 'SI NO QUERIAS ESPACIOS, PARA QUE LLAMAS LA FUNCION'
    if isinstance(list_string_where, list):
        logging.basicConfig(level = logging.INFO, filename= 'formateo.log', filemode='w', format = 'INFORMACION: %(asctime)s %(message)s')
        re_string = re.compile(r'''
\'\'\'.*?\'\'\'| # triples comillas simples y todo lo que esté dentro (non-greedy)
""".*?"""| # triples comillas dobles y todo lo que esté dentro de ellas (non-greedy)
\'.*?\'| # comillas simples y todo lo que esté dentro de ellas (non-greedy)
\".*?\" #comillas dobles y todo lo que esté dentro de ellas (non-greedy)
''',
re.VERBOSE)


        reemplazos = 0
        strings = []


        # recorre la lista dada como argumento. el elemento actual de la
        # lista de strings a partir de ahora será llamado string actual
        for indice, string_where in enumerate( list_string_where ):
            # aqui estarán las ubicaciones de los pares de comillas en 
            # el string where
            string_where, indent_count = guardar_indentacion(string_where) 
            comillas_ubicacion = []
            for coincidencia in re_string.finditer(string_where):
                # añade a la lista antes creada el inicio y el fin de las comillas
                comillas_ubicacion.append([coincidencia.start(), coincidencia.end() - 1])



            ubicacion_re = []
            # aqui van el indice del elemento de antes y despues 
            # de la coincidencia
            if re_excepciones:
                caracter_antes = []
                caracter_despues = []
            
            if comillas_ubicacion:
                for encontrado in re_target.finditer(string_where):
                    for inicio, fin in comillas_ubicacion:


                        # si encuentra la coincidencia pero esta se encuentra dentro
                        # de comillas, no la agrega al array y por lo tanto no
                        # se le agregan espacios a los lados
                        if encontrado.start() > inicio and encontrado.end() > fin + 1:
                            break

                        elif not encontrado.start() > inicio or not encontrado.end() < fin:
                            # # print(f'indice : {indice}')
                            # # print(f'inicio: { inicio }, fin: { fin }')
                            # # print(f'encontrado.start(): {encontrado.start()}')
                            # añade el indice del re_target en el string que se está usando
                            ubicacion_re.append(encontrado.start())

                            # si se definio una excepcion en la llamada de la
                            # funcion, el indice del caracter que le antecede y el que
                            # le sigue se añaden a dos arrais

                            if re_excepciones:
                                caracter_antes.append(encontrado.start() - 1)
                                caracter_despues.append(encontrado.start() + 1)
                    else:
                        continue

            print()
            if not comillas_ubicacion:
                for encontrado in re_target.finditer(string_where):
                    # añade el indice del re_target en el string que se está usando
                    ubicacion_re.append(encontrado.start())

                    # si se definio una excepcion en la llamada de la
                    # funcion, el indice del caracter que le antecede y el que
                    # le sigue se añaden a dos arrais

                    if re_excepciones:
                        caracter_antes.append(encontrado.start() - 1)
                        caracter_despues.append(encontrado.start() + 1)

            # convierte en una lista el string actual
            caracteres_str = list(string_where)

            # si se añadio una regex como excepcion
            if re_excepciones:
                # comprueba si los caracteres de antes y despues de las coincidencias
                # son coincidencia de la regex re_excepciones
                if antes:
                    for posicion in caracter_antes: 
                        excepcion_antes = re_excepciones.search(caracteres_str[posicion])
                        # de ser asi, suma el espacio despues del elemento anterior-1 al
                        # elemento coincidencia, para que quede justo antes del elemento anterior
                        if excepcion_antes:
                            # si el caracter que antecede al caracter antes de re_target es
                            # un espacio, no se añade otro nuevo espacio
                            if not caracteres_str[ posicion - 1] == ' ':
                                caracteres_str[posicion - 1] += ' '
                        elif not excepcion_antes:
                            # si el caracter que antecede al caracter despues de re_target es
                            # un espacio, no se añade otro nuevo espacio
                            if not caracteres_str[ posicion ] == ' ':
                                caracteres_str[posicion ] += ' '

                if despues:
                    for  posicion in caracter_despues: 
                        excepcion_despues = re_excepciones.search(caracteres_str[posicion])
                        # aqui añade el espacio despues del elemento conincidencia
                        # haciendo lo contrario a lo anterior
                        if excepcion_despues:
                            # si el caracter que sigue al caracter despues de re_target es
                            # un espacio, no se añade otro nuevo espacio
                            if not caracteres_str[ posicion  + 1] == ' ':
                                caracteres_str[posicion] += ' '
                                
                        elif not excepcion_despues:
                            # si el caracter que sigue al re_target es
                            # un espacio, no se añade otro nuevo espacio
                            if not caracteres_str[ posicion] == ' ':
                                caracteres_str[posicion - 1] += ' '

                            
                        
            # si no hay re_excepciones
            elif not re_excepciones:
                # añade el espacio justo antes y despues del elemento coincidencia
                for coordenada in ubicacion_re:
                    
                    if antes:
                        # si el caracter que antecede al re_target es
                        # un espacio, no se añade otro nuevo espacio
                        if not caracteres_str[ coordenada - 1] == ' ':
                            caracteres_str[coordenada - 1] += ' '

                    if despues:
                        if len(caracteres_str) > coordenada + 1:
                        # si el caracter que sigue al re_target es
                        # un espacio, no se añade otro nuevo espacio
                            if not caracteres_str[ coordenada + 1] == ' ':
                                caracteres_str[coordenada] += ' '

            # añade al array strings el string actual, pero con los espacios
            caracteres_str = ''.join( caracteres_str ) 
            # si string_where empieza con espacios, remueve esos espacios del principio
            # (para que no sean removidos por el otro while de espacios dobles) y suma 1 
            # a un contador para agregar de nuevo esos espacios luego de las sustituciones

                
            

            # este es caracteres_str sin los espacios dobles
            sin_espacios = quitar_espacio_doble(caracteres_str)
            # aqui regreso los espacios de indentacion al string
            sin_espacios = ' ' * indent_count + sin_espacios

            strings.append(sin_espacios)

            if not caracteres_str == string_where:
                logging.info(f'CAMBIO EN LINEA #{indice + 1}: \n{string_where}\n{caracteres_str}\n\n')





        # retorna el array con todos los strings con los espacios
        return strings

    else:
        raise Exception(f'{list_string_where} is not a list. the first positional argument must be a list.')

re_menos = re.compile('-')
re_mas = re.compile(r'\+')
re_por = re.compile(r'\*')

def formatear(file_route) :
    with open(file_route) as file:
        file = file.read()
        lineas_archivo = file.splitlines()

    strings = añadir_espacios(lineas_archivo, re_igual, re_excepciones = re_operadores)
    strings =añadir_espacios(strings, re_slash )
    strings =añadir_espacios(strings, re_coma, antes = False)
    strings =añadir_espacios(strings, re_mas, re_igual )
    strings =añadir_espacios(strings, re_menos, re_igual )
    strings =añadir_espacios(strings, re_por, re_igual)
    with open(file_route, 'w') as file_target:
        with open(file_route, 'a') as file_target:
            for string in strings:
                file_target.write(string + '\n')


formatear(archivo)
