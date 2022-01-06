import time
import logging
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options

logging.basicConfig(filename='c:\\users\\crist\\desktop\\admisiones.log', format='%(levelname)s %(asctime)s %(message)s', level=logging.INFO, datefmt='%A %d %B %Y; %H.')
opcion_headless = Options()
opcion_headless.add_argument('--headless')

firefox_dir = 'C:\\Users\\crist\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\v2t4u12l.default-release'
profile = FirefoxProfile(firefox_dir)

navigator = webdriver.Firefox(options= opcion_headless,firefox_profile=profile, service_log_path="c:\\users\\crist\\downloads\\creative_projects\\python\\automate_scripts\\geckodriver.log")
navigator.get('https://soft.uasd.edu.do/admision_rne/')
time.sleep(10)

registro = navigator.find_element(By.CSS_SELECTOR,'#hrefNuevo')

color = navigator.execute_script("let documento = document.getElementById('hrefNuevo');let x= window.getComputedStyle(documento); color= x.getPropertyValue('background-color'); return color ")

if color == 'rgb(255, 183, 82)': 
    logging.info('ADMISIONES NO ABIERTAS.')
else:
    navigator.get('https://soft.uasd.edu.do/admision_rne/')
    time.sleep(10)

    registro = navigator.find_element(By.CSS_SELECTOR,'#hrefNuevo')

    color = navigator.execute_script("let documento = document.getElementById('hrefNuevo');let x= window.getComputedStyle(documento); color= x.getPropertyValue('background-color'); return color ")
    if color == 'rgb(255, 183, 82)': 
        logging.info('ADMISIONES NO ABIERTAS.')
    else:
        logging.info('ADMISIONES ABIERTAS.')
        navigator.switch_to.new_window('tab')
        navigator.get('https://web.whatsapp.com')
        time.sleep(5)
        contact = navigator.find_element(By.CSS_SELECTOR,'div._3m_Xw:nth-child(10) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)')
        contact.click()
        
        msg = navigator.find_element(By.CSS_SELECTOR, '._1LbR4 > div:nth-child(2)')
        msg.send_keys('ESTO LO ESTÁ HACIENDO LA COMPUTADORA. Digale a Wanderson que abra la web de la UASD y revise si ya es posible seleccionar.')

        time.sleep(5)
        enviar = navigator.find_element(By.CSS_SELECTOR, 'div._3HQNh:nth-child(2)')
        enviar.click()
        logging.info('MENSAJE ENVIADO')

navigator.quit()

