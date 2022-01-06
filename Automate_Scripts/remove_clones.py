import os, shutil
import re


# ??? la función se encargará de remover músicas duplicadas y cambiar el nombre de las que tienen el (n) en sus nombres.
def quitar_ext_y_parent(ruta_de_musica):
    # ??? cambia a la ruta dada como argumento. es necesario para hacer las comparaciones más adelante.
    os.chdir(ruta_de_musica)
    # ??? expresion regular para encontrar parentesis con un numero adentro. los archivos tienen esto SOLO si están repetidos
    re_parentesis = re.compile('\(\d\)')
    # ??? crea una lista con todos los archivos cuyo nombre termine en .mp3
    musicas_en_carpeta = [musica for musica in os.listdir() if musica.endswith('.mp3') and re_parentesis.search(musica)!=None]
    # ??? crea una lista con la lista de musicas anterior, removiendo el .mp3 y el parentesis si están repetidas
    nombre_de_musica_sin_parentesis = [( numero_de_musica, re_parentesis.sub('', nombre_corregido), nombre_corregido) for numero_de_musica, nombre_corregido in enumerate(musicas_en_carpeta) if re_parentesis.search(nombre_corregido)!=None]

    # ??? crea una lista con todos los archivos cuyo nombre termine en .mp3
    # nombre_de_musica_sin_parentesis = [( numero_de_musica,ruta_de_musica, re_parentesis.sub('', nombre_corregido)) for musica in os.listdir() if musica.endswith('.mp3') and re_parentesis.search(nombre_corregido)==None]
    nombre_de_todas_las_musicas = [ musica for musica in os.listdir() if musica.endswith('.mp3') and re_parentesis.search(musica) == None]
    # ??? retorna una lista con los nombres de las musicas en la carpeta especificada y los nombres de esas musicas sin el .mp3 y el nombre de todas las músicas que no tienen parentesis
    return [musicas_en_carpeta, nombre_de_musica_sin_parentesis, nombre_de_todas_las_musicas, ruta_de_musica]


     
# ??? toma como parametro dos listas, que son el return de la funcion quitar_ext_y_parent.
def eliminar_duplicados(lista_musica_descargas = quitar_ext_y_parent('c:\\users\\crist\\downloads'), lista_musica = quitar_ext_y_parent('c:\\users\\crist\\music')):

    # ??? aqui cambio el nombre de los argumentos a otros
    # ??? esta variable debe contener la musica de la carpeta downloads
    musica_descargas = lista_musica_descargas
    # ??? esta debe contener la musica de la carpeta music
    musica = lista_musica

    # ??? esta lista contiene el nombre de las musicas sin el parentesis
    # ??? esta variable es para usarla en el proceso de cambio de nombre
    for indice, nombre, con_parentesis in musica[1]:
        if nombre in musica_descargas[1]:
            # ??? elimina la musica
            os.chdir(musica_descargas[3])
            os.unlink(musica_descargas[3] + '\\' + con_parentesis)
            print(con_parentesis, ' ha sido eliminado')

    for nombre in musica[2]:
        

        if nombre in musica_descargas[2]:
            # ??? elimina la musica
            os.chdir(musica_descargas[3])
            os.unlink(musica_descargas[3] + '\\' + nombre)
            print(nombre, ' ha sido eliminado')

    for indice, nombre, con_parentesis in musica[1]:
            

        os.chdir(musica[3])
        os.unlink(musica[3] + '\\' + con_parentesis)
        print(con_parentesis, ' ha sido eliminado')


    for indice, nombre, con_parentesis in musica_descargas[1]:
            

        os.chdir(musica_descargas[3])
        os.unlink(musica_descargas[3] + '\\' + con_parentesis)
        print(con_parentesis, ' ha sido eliminado')


    
    for nombre in musica[2]:
        if nombre.endswith('.mp3.mp3'):
            try:
                os.chdir(musica[3])
                os.unlink(musica[3] + '\\' + nombre)
                print(nombre, ' ha sido eliminado')
            except:
                continue


    for nombre in musica_descargas[2]:
        if nombre.endswith('.mp3.mp3'):

            try:
                os.chdir(musica_descargas[3])
                os.unlink(musica_descargas[3] + '\\' + nombre)
                print(nombre, ' ha sido eliminado')
            except:
                continue




    




eliminar_duplicados()
