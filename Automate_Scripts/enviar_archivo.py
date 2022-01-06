import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

# ??? este es la ruta del perfil default-release de firefox, donde debe estar abierto el whatsapp
firefox_dir = 'C:\\Users\\crist\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\v2t4u12l.default-release'
# ??? objeto tipo perfil de firefox para selenium
profile = FirefoxProfile(firefox_dir)
# ??? el navegador que usará selenium, con el perfil default-release
navigator = webdriver.Firefox(firefox_profile=profile)
# ??? abrir whatsapp web
navigator.get('https://web.whatsapp.com')
# ??? esperar 10 segundos a que carge, para no provocar NoSuchElementException
time.sleep(5)
# ??? el contacto a quien debe ser enviado el archivo, seleccionado por selector css
# NNN debo cambiar el contacto
contact = navigator.find_element(By.CSS_SELECTOR,'div._3m_Xw:nth-child(10) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)')
# ??? hacer click en el elemento "contacto" 
contact.click()


# msg = navigator.find_element(By.CSS_SELECTOR, '._1LbR4 > div:nth-child(2)')
# msg.send_keys('ESTO LO ESTÁ HACIENDO LA COMPUTADORA. Digale a Wanderson que abra la web de la UASD y revise si ya es posible seleccionar.')

# time.sleep(5)
# enviar = navigator.find_element(By.CSS_SELECTOR, 'div._3HQNh:nth-child(2)')
# enviar.click()

# navigator.quit()

