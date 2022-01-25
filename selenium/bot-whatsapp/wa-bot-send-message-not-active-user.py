from selenium import webdriver # Se importa libreria de selenium para controlar el navegador
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time,sys #Librería para utilidades de tiempo



# Función para abrir un chat nuevo si el usuario no se encuentra en una conversación abierta.
def new_chat(user_name): 
    new_chat = browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    new_chat.click()
    time.sleep(1)
    new_user = browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    new_user.send_keys(user_name)
    try:
        user_name = browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        user_name.click()
    except NoSuchElementException:
        print('User:"{}" not found in the contact list'.format(user_name))
    except Exception as e:
        browser.close()
        print(e)
        sys.exit()
if __name__ == '__main__':
    options = webdriver.FirefoxOptions()
    options.add_argument('--user-data-dir=/home/faem/.mozilla/firefox/oidtfv1j.default-release')
    options.add_argument('--profile-directory=default-release')

    browser = webdriver.Firefox(executable_path='/home/faem/dev/bots/selenium/geckodriver', options=options)# Se define el navegador que se va a usar- En este caso brave con el driver de Chrome.
    url = 'https://web.whatsapp.com/' # Se define el url para acceder a la página
    browser.get(url)# Se accede a la página con un método get.

    # Se deja este tiempo de espera en el código para poder escanear el QR y acceder a la cuenta
    time.sleep(15)
    user_name_list = ['Bot']
    for user_name in user_name_list:
        try:
            #Se selecciona el objeto inspeccionando el html y copiando el xpath, se le asigna a una variable.
            user_name = browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
            #Se hace click en el div para acceder a la conversación
            user_name.click()
        except NoSuchElementException as se:
            new_chat(user_name)
        
        #Se selecciona el elemento para escribir el mensae y se asigna a una variabke 
        message_box = browser.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]')
        # con send keys se ingresan datos cómo si vinieran desde el teclado. Texto y ENTER
        message = 'Este es un mensaje de bot'
        message_box.send_keys(message + Keys.RETURN)
    browser.close()
