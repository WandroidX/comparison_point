# modulos importados
import os
import warnings
from time import sleep
from selenium import webdriver
from listmusic import list_music
from move_files import sort_music
import os, re, pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# warnings.filterwarnings("ignore", category=DeprecationWarning)
y2mate=1
browser=webdriver.Firefox(service_log_path="C:\\Users\\crist\\Downloads\\Proyectos Creativos\\Python\\Automate Scripts\\geckodriver.log")
browser.get('https://youtube.com/playlist?list=PLpqO7dRg1jAd0QD05-gT_GLIs0e4fhQWh')
seek=browser.find_elements_by_id('video-title')
# this is the array where will be saved the music names and links of they
namelink=[[],[]]
altsustitutions=[[], []]
signos=["""\u0028""", """\u0029""","""\u005b""","""\u005d""","""\u007b""","""\u007d""", """\u002e""", """\u007c""","""\u002d""",'\\'+"""\u005c""","""\u005f""", """\u002f""","""\u003a""", """\u007e""","""\u002c""","""\u002b""","""\u003b""","""\u300d""","""\u300c""","""\u300e""","""\u300f""","\u2013",'&','#',"'",'"','´','^','*','<','>','%','$','°',';',':','¨','`','@','\uff1c','\uff1e','!','¡','¿','?','\u2019','\u2502']



for links in range(0,len(seek)):
        


    if namelink==[[],[]]:
        for enlace in range(0,len(seek)):
            namelink[0].append(seek[enlace].text)
            namelink[1].append(seek[enlace].get_attribute('href'))



        for namemusic in range(0,len(namelink[0])):
            for title in range(0,len(signos)):
                sign=signos[title]
                sustitution=namelink[0][namemusic].replace(sign, '')
                sustitution=sustitution.replace(sign, '')
                namelink[0][namemusic]=sustitution


            while '  ' in sustitution:
                sustitution=sustitution.replace('  ',' ')
            namelink[0][namemusic]=sustitution
            altsustitutions[0].append(sustitution.replace('ft','con'))
            altsustitutions[1].append(sustitution.replace('ft','Con'))

        
# if doesn exist the file, create it        
        if  not os.path.exists('c:\\users\\crist\\desktop\\youtube_music.txt'):
            file=open('c:\\users\\crist\\desktop\\youtube_music.txt','w')
            file.close()

    
    with open('c:\\users\\crist\\desktop\\youtube_music.txt','r',encoding='utf-8') as linea:
    
        lines=linea.readlines()
        for linea in range(0,len(lines)):
            lines[linea]=lines[linea].replace('\n','')




    if len(lines)!=0:

        for musicas in list_music():
            musicas=musicas.replace('.mp3','')
            while '  ' in musicas:
                musicas=musicas.replace('  ',' ')

            with open('c:\\users\\crist\\desktop\\youtube_music.txt', 'a', encoding='utf-8') as writ:

                if musicas in lines:
                    continue
                else:
                    writ.write(musicas+'\n')

    else:
        for musicas in list_music():
            musicas=musicas.replace('.mp3','')
            write=0
            with open('c:\\users\\crist\\desktop\\youtube_music.txt', 'a', encoding='utf-8') as writ:

                with open('c:\\users\\crist\\desktop\\youtube_music.txt','r',encoding='utf-8') as linea:

                    lines=linea.readlines()
                    for linea in range(0,len(lines)):
                        lines[linea]=lines[linea].replace('\n','')

                    

                if musicas in lines:
                    continue
                else:
                    print(musicas)

                    while '  ' in musicas:
                        musicas=musicas.replace('  ','')
                    writ.write(musicas+'\n')

    # with open('c:\\users\\crist\\desktop\\youtube_music.txt','r',encoding='utf-8') as linea:

        # lines=linea.readlines()


        # for linea in range(0,len(lines)):
            # lines[linea]=lines[linea].replace('\n','')



# if the file exist, get the lines of that
    
    if len(lines)>links:
        if namelink[0][links] in lines: 
            continue
        if altsustitutions[0][links] in lines:
            continue
        if altsustitutions[1][links] in lines:
            continue


        else:

    # open the file where will be wrote down the musics downladed
            


            browser.get('https://www.y2mate.com/es57')

    # # move the mouse to superior left corner and click, this is to change the current window to y2mate window
            pyautogui.moveTo(53,7)
            pyautogui.click()
            pyautogui.moveTo(70,329)
            pyautogui.click()


            searchvid=browser.find_element_by_id('txt-url')
            searchvid.send_keys(namelink[1][links])
            searchvid.submit()
            element = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.LINK_TEXT, "Audio")))
            audio=browser.find_element_by_link_text('Audio')
            audio.click()



            othername=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div[4]/div/div[1]/div[1]/div/b')

            namelink[0][links]=othername.text

            for namemusic in range(0,len(namelink[0])):
                for title in range(0,len(signos)):
                    sign=signos[title]
                    sustitution=namelink[0][namemusic].replace(sign, '')
                    sustitution=sustitution.replace(sign, '')
                    namelink[0][namemusic]=sustitution


                while '  ' in sustitution:
                    sustitution=sustitution.replace('  ',' ')
                namelink[0][namemusic]=sustitution

            if namelink[0][links] in lines: 
                continue
            if altsustitutions[0][links] in lines:
                continue
            if altsustitutions[1][links] in lines:
                continue


            download=browser.find_element_by_css_selector('#dbtn-mp3128')
            download.click()
            element = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.btn-file')))
            download_two=browser.find_element_by_css_selector('.btn-file')
            download_two.click()

    # click in save file and accept
            
            if y2mate==1:
                pyautogui.moveTo(509, 411, duration=5)
                pyautogui.doubleClick()
                pyautogui.moveTo(523, 440)
                pyautogui.click()
                pyautogui.moveTo(774, 519)
                pyautogui.click()
                y2mate=0

    # define y to after if is neccesary change its value
            y=1
            for x in range(0,y):
                sleep(5)

                for folder, subfolder, archivos in os.walk('c:\\users\\crist\\downloads'):

    # if the music that wants to download still isn downloaded, the bucle start again
                    for archivo in range(0,len(archivos)):
                        archivos[archivo]=archivos[archivo].replace('.mp3','')

                    if 'y2mate.com - '+ namelink[0][links] in archivos:
                        print('a music has been downloaded: ' + namelink[0][links])
                        with open('c:\\users\\crist\\desktop\\youtube_music.txt', 'a', encoding='utf-8') as downmus:
                            downmus.write(namelink[0][links]+'\n')

                        break
                    else:
                        y=y+1
                

sort_music()




    




