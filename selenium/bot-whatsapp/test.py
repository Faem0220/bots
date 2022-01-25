from selenium import webdriver # Se importa libreria de selenium para controlar el navegador
from selenium.webdriver.common.keys import Keys
import time #Librería para utilidades de tiempo

browser = webdriver.Firefox(executable_path='/home/faem/dev/bots/selenium/geckodriver')# Se define el navegador que se va a usar- En este caso brave con el driver de Chrome.
url = 'https://web.whatsapp.com/' # Se define el url para acceder a la página
browser.get(url)# Se accede a la página con un método get.


time.sleep(15)# Se deja este tiempo de espera en el código para poder escanear el QR y acceder a la cuenta.30SEC

user_name = 'Información automática'# Se asigna el nombre el chat 

user = browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))# Se busca en en html en formato xpath
user.click()#Se hace click en el div para acceder a la conversación

message_box = browser.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]')
for i in range(20):
    message_box.send_keys('new(Numa);Numa^.edad:=actualizarEdad(2021)'+ Keys.RETURN)
    time.sleep(5)

print('Listo')