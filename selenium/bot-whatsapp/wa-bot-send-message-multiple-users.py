from selenium import webdriver # Se importa libreria de selenium para controlar el navegador
from selenium.webdriver.common.keys import Keys
import time #Librería para utilidades de tiempo

browser = webdriver.Firefox(executable_path='/home/faem/dev/bots/selenium/geckodriver')# Se define el navegador que se va a usar- En este caso brave con el driver de Chrome.
url = 'https://web.whatsapp.com/' # Se define el url para acceder a la página
browser.get(url)# Se accede a la página con un método get.


time.sleep(15)# Se deja este tiempo de espera en el código para poder escanear el QR y acceder a la cuenta.30SEC
user_name_list = ['USERS']
for user_name in user_name_list:
    #Se selecciona el objeto inspeccionando el html y copiando el xpath, se le asigna a una variable.
    user_name = browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
    user_name.click()#Se hace click en el div para acceder a la conversación
    #Se selecciona el elemento para escribir el mensae y se asigna a una variabke 
    message_box = browser.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]')
    # con send keys se ingresan datos cómo si vinieran desde el teclado. Texto y ENTER
    message = 'Este es un mensaje de bot'
    message_box.send_keys(message + Keys.RETURN)
