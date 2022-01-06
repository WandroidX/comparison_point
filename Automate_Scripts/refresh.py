import os, sys, re
from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException
import time

# ??? FUNCIONAMIENTO: ABRE EL ARCHIVO HTML PASADO COMO ARGUMENTO EN EL NAVEGADOR. USANDO LA FUNCION "OPEN" LO ABRE EN PYTHON JUNTO LOS ARCHIVOS CSS Y JS ENLAZADOS EN ESTE. LUEGO EXTRAE EL TEXTO DE LOS MISMOS  Y ESPERA UNAS DECIMAS DE SEGUNDO. FINALMENTE LOS ABRE NUEVAMENTE CON PYTHON, EXTRAE SU TEXTO Y COMPARA EL TEXTO DE LOS ABIERTOS PRIMERO CON LOS ABIERTOS AL FINAL. SI DETECTA CAMBIOS, REFRESCA LA VENTANA DE SELENIUM.

 
# ??? esta función es para abrir el archivo pasado como parámetro y retornar el texto de este
def read_file(archivo):
    with open(archivo) as want_text:
        text_of_archivo = want_text.read()
    return text_of_archivo

# ??? el argumento pasado desde la consola es un nombre de archivo, que será abierto mas tarde
file_path = sys.argv[1]
# ??? verifica si el nombre de archivo pasado como argumento existe
if os.path.exists(file_path):

    if len(sys.argv)<2:
        raise Exception('need an argument: FILE_PATH')

    if len(sys.argv)>2:
        raise Exception('too many arguments')

    else:

# ??? esta variable es una expresion regular de las etiquetas <link> en los archivos html
        re_link = re.compile(r'(<link .*>)')
# ??? esta variable es una expresion regular que usaré para extraer el "href" de las etiquetas link
        re_link_href = re.compile(r'(href=".*\.\w{1,4}")')
# ??? esta variable es el nombre de archivo pasado en la consola, pero reemplazando las "/" por "\\"
        file_url = sys.argv[1].replace('\\','/')
# ??? esta variable es una expresion regular de las etiquetas <script> en los archivos html
        re_script = re.compile(r'(<script .*>)')
# ??? esta variable es una expresion regular que usaré para extraer el "src" de las etiquetas script
        re_script_src = re.compile(r'(src=".*\.\w{2,4}")')

# ??? variable que contiene la ventana de selenium a usar
        browser = webdriver.Firefox()
# ??? abrir el archivo en el navegador de selenium, usando como url "file:///" debido a que es un archivo y concatenandolo con el parametro con "\\" luego de reemplazar los espacios en blanco en el nombre del archivo por "%20"
        browser.get('file:///'+file_url.replace(' ', '%20'))

# ??? un bucle infinito para comparar archivos
        while True: 
# ??? comprobar si la ventana del navegador sigue abierta
            try:
                browser.current_window_handle
# ??? si no está abierta, terminar el script 
            except NoSuchWindowException:
                exit()
# ??? cambiar el directorio de trabajo actual a la carpeta del archivo argumento 
            os.chdir(os.path.dirname(file_path))
# ??? abrir el archivo html y leer su contenido
            with open(file_path,'r',encoding = 'utf-8') as html_file:
                html_text = html_file.read()

# ??? encuentra todas las etiquetas "link" en el texto del html
            findall_re_link = re_link.findall(html_text)
# ??? encuentra todas las etiquetas "script" en el texto del html
            findall_re_script = re_script.findall(html_text)


            if len(findall_re_link)>0:
# ??? aquí se almacenarán el texto que contiene el "src" en la etiqueta "link"
                css_paths = []
# ??? un for range con la longuitud de findall_re_link                
                for index in range(len(findall_re_link)):
# ??? esta variable es el resultado de buscar el "href" en las etiquetas "link" y tomar el grupo 1 en la expresion regular
                    enlace = re_link_href.search(findall_re_link[index]).group(1)
# ??? añade a la lista "css_paths" el resultado de buscar con regex el valor de "href" en la variable enlace
                    css_paths.append(re.compile(r'=(.*)').search(enlace).group(1))
# ??? reemplaza las comillas dobles por nada en "css_paths[index]"
                    css_paths[index] = css_paths[index].replace('"', '')
                   

            if len(findall_re_script)>0:
# ??? aquí se almacenarán el texto que contiene el "src" en la etiqueta "script"
                js_paths = []
# ??? un for range con la longuitud de findall_re_script                
                for index in range(len(findall_re_script)):
# ??? esta variable es el resultado de buscar el "src" en las etiquetas "script" y tomar el grupo 1 en la expresion regular
                    enlace = re_script_src.search(findall_re_script[index]).group(1)
# ??? añade a la lista "s_paths" el resultado de buscar con regex el valor de "src" en la variable enlace
                    js_paths.append(re.compile(r' = (.*)').search(enlace).group(1))
# ??? reemplaza las comillas dobles por nada en "js_pathss[index]"
                    js_paths[index] = js_paths[index].replace('"', '')

            if len(findall_re_link)>0:
# ??? recorre css_paths con la funcion range
                for ruta in range(len(css_paths)):
# ??? comprueba si no existe la ruta de archivo dado
                    try:
                        if not os.path.exists(css_paths[ruta]):
# ??? cambia su valor a ''
                            css_paths[ruta] = ''
                            
# ??? si se produce IndexError, cancela el bucle for. esto pasa si no hay 
                    except IndexError:
                        break

# ??? crea una lista con el texto de todas las hojas de estilo en el html
                css_text = [read_file(css_paths[x]) for x in range(len(css_paths)) ]

            if len(findall_re_script)>0:
                for ruta in range(len(js_paths)):
                    try:
# ??? comprueba si no existe la ruta de archivo dado
                        if not os.path.exists(js_paths[ruta]):
# ??? cambia su valor a ''
                            js_pathss[ruta] = ''
# ??? si se produce IndexError, cancela el bucle for. esto pasa si no hay 
                    except IndexError:
                        break
# ??? crea una lista con el texto de todos los archivos de javascript en el html
                js_text = [read_file(js_paths[x]) for x in range(len(js_paths)) ]


# ??? comprueba que la longuitud de la lista con los textos
            if len(css_text)>0 or len(js_text)>0:
# ??? el script se congela por casi un segundo. esto es para dar tiempo a que ocurran los cambios en el archivo y poder notarlos más adelante
                time.sleep(0.8)
            else:
# ??? si no hay texto de css o de javascript, el script se congela por 0.2 segundos. esto es suficiente para notar cambios en el html, pero no en el javascript o el css
                time.sleep(0.2)

# ??? comprueba que "findall_re_link" no está vacio
            if len(findall_re_link)>0:
# ??? toma por segunda vez el texto de las hojas de estilo enlazadas al html
                css_text_2 = [read_file(css_paths[x]) for x in range(len(css_paths)) ]

                for texto in range(len(css_text)):
# ??? comprueba si existe diferencia entre el texto abierto hace casi un segundo y el abierto ahora
                    if css_text[texto] != css_text_2[texto]:
# ??? si hay diferencias, refresca la ventana abierta por selenium
                        browser.refresh()
# ??? y se salta todo el codigo de debajo
                        continue


# ??? comprueba que "findall_re_script" no está vacio
            if len(findall_re_script)>0:
# ??? toma por segunda vez el texto de los archivos js enlazados al html
                js_text_2 = [read_file(js_paths[x]) for x in range(len(js_paths)) ]
                for texto in range(len(js_text)):
# ??? comprueba si existe diferencia entre el texto abierto hace casi un segundo y el abierto ahora
                    if js_text[texto] != js_text_2[texto]:
# ??? si hay diferencias, refresca la ventana abierta por selenium
                        browser.refresh()
# ??? y se salta todo el codigo de debajo
                        continue

# ??? abre por segunda vez el archivo html pasado como parametro
            with open(file_path,'r',encoding = 'utf-8') as html_file_2:
                html_text_2 = html_file_2.read()

# ??? comprueba si hay diferencias entre los dos html abiertos
            if html_text != html_text_2:
# ??? si hay diferencias, refresca la ventana abierta por selenium
                browser.refresh()

# ??? si la ruta pasada como parametro no existe, salta una exepcion que imprime el argumento insertado desde la consola
else:
    print(sys.argv[1])
    raise Exception('that file doesnt exist')
