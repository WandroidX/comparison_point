import shutil, os

# ??? toma como primer argumento la ruta donde está la musica a ser movida y renombrada, y como segundo argumento a donde será movida
def sort_music(ruta_a_ordenar = 'c:\\users\\crist\\downloads', ruta_a_mover = 'c:\\users\\crist\\music'):


    # ??? cambia el directorio de trabajo a la ruta del primer argumento, para no tener que escribir el nombre de la variable a cada rato
    os.chdir(ruta_a_ordenar)
    # ??? esta variable aumenta en 1 cada vez que se mueve una música a la ruta_a_mover
    n_moved=0

    # ??? esta lista contiene las músicas que serán movidas, las cuales empiezan en y2mate.com - y terminan en .mp3
    movible =  [archivo for archivo in os.listdir(ruta_a_ordenar) if archivo.endswith('.mp3') and archivo.startswith('y2mate.com - ')]



    # ??? recorre la lista de musicas movibles y las mueve. además aumenta el valor de n_moved en 1
    for musica in movible:
        shutil.move(musica, ruta_a_mover+ '\\' + musica.replace('y2mate.com - ', ''))
        n_moved += 1


    # ??? si se ha movido alguna música, imprime su nombre y desde donde se movió
    if n_moved!=0:
        print('se han movido los siguientes %d archivos:' % (n_moved))
        for nombre_musica in movible:
            print('%s' % (nombre_musica))


