# ??? modulos importados
import os, sys, re, emoji, logging 
from redondear import RoundTo
from time import sleep
from selenium import webdriver
from listmusic import list_music
from move_files import sort_music
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException as nsee
from remove_clones import eliminar_duplicados
from remove_clones import quitar_ext_y_parent
from selenium.webdriver.firefox.options import Options

### FUNCIONES CREADAS PARA EL SCRIPT

# ??? esta funcion remueve los emojis de los nombres de las canciones,
# un dolor de cabeza menos para mi
def remover_emoji(texto):
    texto = list(texto)
    for indice, letra in enumerate(texto):
        if letra in emoji.UNICODE_EMOJI['en']:
            texto[indice] = ''
    return ''.join(texto)

# ???  esta funcion quita los dos ultimos digitos de un numero dado
# ???  su parametro es un string
def multiplo_de_cien(numberstr):
    # ??? convierte el parametro en una lista
    strlist=list(numberstr)
    # ??? luego sustituye sus dos ultimos caracteres por 0
    strlist[-2]='0'
    strlist[-1]='0'
    # ??? luego junta todos los elementos de la lista
    string=''.join(strlist)
    # ??? ahora esta variable es igual al entero del numero juntado anteriormente 
    # ??? entre 100 convertido a str.
    string=str(int(string)/100)
    # ??? divide el texto (o numero) en el "."
    string=string.split('.')
    # ??? descarta lo que está despues del punto (es decir, "string[1]")
    string=string[0]
    # ??? retorna el string convertido en entero
    return int(string)
# ??? esta es la ruta del perfil que deseo usar para abrir el navegador con selenium


def quitar_signos(objetivo):
    for indice, contenido in enumerate(objetivo):
        for sign in signos:
            if sign in contenido:
                # ??? esta variable es el titulo de video, pero quitandole el signo actual
                sustitution = contenido.replace(sign, '')
                # ??? mientras hayan dos espacios en la cadena sustituida, los reemplaza por 1
                while '  ' in sustitution:
                    sustitution = sustitution.replace('  ', ' ')
                # ??? esto se requiere para capturar el texto sin signo arrojado por
                # la sustitucion
                contenido = sustitution
            # ??? ahora cambia el título sin signos por sí mismo sin dobles espacios.
        objetivo[indice]= contenido    


# ??? aqui se guardarán las musicas descargadas, 
# para luego escribirlas en el archivo de logs
musica_descargada = []

# ??? estas dos lineas son para pasar al argumento options en el webdriver y me permitirán que el navegador se ejecute sin interfaz grafica
opcion_sin_cabeza = Options()
opcion_sin_cabeza.add_argument('--headless')






# aqui elimino las musicas duplicadas (en caso de que las haya)
sort_music()
eliminar_duplicados()

firefox_dir = 'C:\\Users\\crist\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\v2t4u12l.default-release'
# ??? aqui paso como parametro la ruta del perfin
profile = FirefoxProfile(firefox_dir)
# ??? esta variable es el navegador que recibirá las ordenes más adelante
browser=webdriver.Firefox(options = opcion_sin_cabeza, service_log_path = "C:\\Users\\crist\\Downloads\\creative_projects\\Python\\automate_scripts\\geckodriver.log", firefox_profile = profile)
# ??? verifica si se pasó un argumento desde la consola
if len(sys.argv) == 2:
    # ???  abre la playlist dada desde la consola de comandos
    browser.get(sys.argv[1])
# ??? si no se pasan argumentos desde la consola
else: 
    # ???  abre la playlist dada desde la consola de comandos
    browser.get('https://youtube.com/playlist?list=PLpqO7dRg1jAd0QD05-gT_GLIs0e4fhQWh')
# ??? esta lista contiene los caracteres que son removidos por y2mate al descargar la música.
signos=["\u25cf", """\u0028""","""\u0029""","""\u005b""","""\u005d""","""\u007b""","""\u007d""", """\u002e""", """\u007c""","""\u002d""",'\\'+"""\u005c""","""\u005f""", """\u002f""","""\u003a""", """\u007e""","""\u002c""","""\u002b""","""\u003b""","""\u300d""","""\u300c""","""\u300e""","""\u300f""","\u2013",'&','#',"'",'"','´','^','*','<','>','%','$','°',';',':','¨','`','@','\uff1c','\uff1e','!','¡','¿','?','\u2019','\u2502']
# ??? esta variable contiene el numero de videos que hay en la playlist
numero_de_videos=browser.find_element(By.XPATH, '//*[@id="stats"]/yt-formatted-string[1]/span[1]').text
# ??? esta variable convierte en multiplo de cien el numero de videos
numero_de_scroll=multiplo_de_cien(numero_de_videos)
# ??? si la variable es mayor o igual que uno
if numero_de_scroll>=1:
    for scrolls in range(numero_de_scroll):
        # ??? ejecuta un script de js para arrastrar la barra de desplazamiento al final
        browser.execute_script("window.scrollTo(0, 10000)")
        # ??? esto es para esperar a que carguen los videos
        sleep(5)
# ??? esta variable contiene todos los videos en la playlist
seek=browser.find_elements(By.ID, 'video-title')
# ??? en la primera lista dentro de esta lista están los títulos de todos los videos y en la segunda se encuentran sus enlaces.
namelink=[[remover_emoji(seek[enlace].text) for enlace in range(len(seek))], [seek[enlace].get_attribute('href') for enlace in range(len(seek))]]


# ??? aqui se remueven los signos de los nombres de las canciones, 
# para poder comparar si están descargadas o no en el futuro
for numero_de_musica in range(len(namelink[0])):
    titulo = namelink[0][numero_de_musica]
    for sign in signos:
        if sign in titulo:
            # ??? esta variable es el titulo de video, pero quitandole el signo actual
            sustitution=titulo.replace(sign, '')
            # ??? mientras hayan dos espacios en la cadena sustituida, los reemplaza por 1
            while '  ' in sustitution:
                sustitution=sustitution.replace('  ', ' ')
            # ??? esto se requiere para capturar el texto sin signo arrojado por
            # la sustitucion
            titulo=sustitution
        # ??? ahora cambia el título sin signos por sí mismo sin dobles espacios.
    namelink[0][numero_de_musica]= titulo    

# ??? lista de las musicas descargadas y que están en la carpeta Músicas
lista_de_musica_music = list_music()

for indice, musicas in enumerate(lista_de_musica_music):
    musicas = musicas.replace('.mp3', '')
    # ??? elimina los espacios dobles en el nombre de la musica
    while '  ' in musicas:
        musicas=musicas.replace('  ', ' ')
    lista_de_musica_music[indice] = musicas

    with open('c:\\users\\crist\\desktop\\downloaded_music.txt', 'w', encoding='utf-8') as objetivo_escritura:
        objetivo_escritura.write("\n".join(lista_de_musica_music))


for links in range(len(seek)):
    # ??? lista de las musicas descargadas y que están en la carpeta Músicas
    lista_de_musica_music = list_music()

    with open('c:\\users\\crist\\desktop\\downloaded_music.txt', 'r',encoding='utf-8') as archivo_nombre_musicas:
        lista_lineas = archivo_nombre_musicas.read()
        lista_lineas = lista_lineas.split('\n')

    if namelink[0][links] in lista_lineas: 
        continue
    else:
        # ??? abrir y2mate
        browser.get('https://www.y2mate.com/es57')
        # ??? encuentra el input donde se debe poner el enlace del video a descargar
        searchvid=browser.find_element(By.ID, 'txt-url')
        # ??? escribe en ese input el enlace del video
        searchvid.send_keys(namelink[1][links])
        # ??? y lo envia para que y2mate busque el video
        searchvid.submit()
        # ??? espera a que aparezca "Audio", porque a veces tarda un poco en apareceer
        element = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.LINK_TEXT, "Audio")))
        # ??? este es el nombre original del video de youtube, el nombre que tendrá la música descargada de y2mate.  
        othername=browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div[4]/div/div[1]/div[1]/div/b')

        # ??? cambia en la lista el título en youtube (el falso) por el verdadero(el obtenido de y2mate)
        namelink[0][links]=othername.text
        

        for sign in signos:
            sustitution=namelink[0][links].replace(sign, '')
            sustitution=sustitution.replace(sign, '')
            namelink[0][links]=remover_emoji(sustitution)


        while '  ' in sustitution:
            sustitution=sustitution.replace('  ', ' ')

        namelink[0][links]=sustitution

        if namelink[0][links] in lista_lineas: 
            continue

        else:
            # ??? encuentra el "botón" llamado Audio y lo clickea
            audio=browser.find_element(By.LINK_TEXT, 'Audio')
            audio.click()

            # ??? ahora encuentra el botón para descargar la música en calidad 128k y lo clickea
            
            download=browser.find_element(By.CSS_SELECTOR, '#dbtn-mp3128')
            download.click()
            # ??? espera 3 segundos. no es webdriver.wait porque el script se pararía si y2mate da error al descargar la música
            sleep(3)
            # ??? intenta buscar el segundo botón de descarga y clickearlo
            try:
                download_two=browser.find_element(By.CSS_SELECTOR, '.btn-file')
                download_two.click()
                sleep(2)
                # ??? id de la primera ventana del webdriver
                ventanas = browser.window_handles

                # ??? cierra todas las demás ventanas del webdriver, a excepcion de la primera abierta
                for indice, identificador in enumerate(ventanas):
                    if indice!=0:
                        browser.switch_to.window(identificador)
                        browser.close()
                else:
                    browser.switch_to.window(ventanas[0])

                contador = 0
                while True:
                    sleep(1)
                    contador += 1
                    # ??? crea una lista con los archivos en la carpeta downloads del usuario crist.
                    # ??? con un list comprehend que añade la variable archivo a la lista si esta es un archivo
                    musica_en_downloads = list_music('c:\\users\\crist\\downloads')

                    
                    # ??? comprueba si el nom
                    musica_descargando = 'y2mate.com - '+ namelink[0][links]+'.mp3'
                    # ??? aquí estará el nombre de la musica descargandose, pero con .part, para saber si se está descargando

                    if musica_descargando in musica_en_downloads:
                        os.chdir('c:\\users\\crist\\downloads')
                        musica_descargando_con_part = musica_descargando + '.part' 
                        
                        
                        if not musica_descargando_con_part in os.listdir():

                            print('una música se ha descargado: ' + namelink[0][links])
                            # ??? abre el archivo donde deben estar los nombres de música
                            # en modo append y escribe en él el nombre de la música descargada
                            with open('c:\\users\\crist\\desktop\\downloaded_music.txt', 'a', encoding='utf-8') as archivo_nombre_musicas:
                                archivo_nombre_musicas.write(namelink[0][links]+'\n')
                                musica_descargada.append(namelink[0][links])
                            # ??? añade la musica descargada a una lista y ordena y elimina los duplicados de músicas. a continuacion termina el bucle
                            # musica_descargada.append(namelink[0][links])
                            sort_music()
                            eliminar_duplicados()
                            break

                    # ??? esto en caso de que no empiece a descargarse la música
                    # al clickar en descargar
                    elif contador == 10 and musica_descargando not in musica_en_downloads:
                        browser.refresh()
                        # ??? inserta en el input de descargar videos el enlace
                        # del video a descargar y lo envia
                        searchvid=browser.find_element(By.ID, 'txt-url')
                        searchvid.send_keys(namelink[1][links])
                        searchvid.submit()
                        # ??? espera a que aparezca "Audio", porque a veces tarda un poco en apareceer
                        element = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.LINK_TEXT, "Audio")))

                        # ??? encuentra el "botón" llamado Audio y lo clickea
                        audio=browser.find_element(By.LINK_TEXT, 'Audio')
                        audio.click()

                        # ??? ahora encuentra el botón para descargar 
                        # la música en calidad 128k y lo clickea
                        download=browser.find_element(By.CSS_SELECTOR, '#dbtn-mp3128')
                        download.click()
                        sleep(3)
                        # ??? intenta buscar el segundo botón de descarga y clickearlo
                        try:
                            download_two=browser.find_element(By.CSS_SELECTOR, '.btn-file')
                            download_two.click()
                            sleep(2)
                            # ??? id de la primera ventana del webdriver
                            ventanas = browser.window_handles

                            # ??? cierra todas las demás ventanas del webdriver,
                            # a excepcion de la primera abierta
                            for indice, identificador in enumerate(ventanas):
                                if indice!=0:
                                    browser.switch_to.window(identificador)
                                    browser.close()
                            # ??? al finalizar el for, vuelve a la primera ventana abierta
                            # por el webdriver de selenium
                            else:
                                browser.switch_to.window(ventanas[0])
                        # ??? si no encuentra el segundo botón de descarga 
                        # (solo pasa si da el error en y2mate), salta a 
                        # la siguiente música
                        except nsee:
                            continue
                                    


                    
            # ??? si no encuentra el segundo botón de descarga 
            # (solo pasa si da el error en y2mate), salta a 
            # la siguiente música
            except nsee:
                continue

# ??? añade la lista con las músicas descargada al archivo de logs
if musica_descargada != []:
    # ??? usando como separador de cada elemento una coma, una nueva linea y
    # un tab para que se vea más vistoso
    musica_unida = ',\n\t'.join(musica_descargada)

    logging.basicConfig(filename='c:\\users\\crist\\desktop\\musica_descargada.log', filemode='a', format='%(levelname)s: %(asctime)s %(message)s', level= logging.INFO, datefmt='%A %d de %B del año %Y; %H')

    logging.info(
f'''Musica descargada: 
    {musica_unida}.

''')

# ??? cierra el navegador al finalizar
browser.quit()








