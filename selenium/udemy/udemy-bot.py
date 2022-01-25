from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import date

# Se crea una variable para el controlador del navegador (firefox)
browser = webdriver.Firefox(executable_path='/home/faem/dev/bots/selenium/geckodriver')
date = date.today().isoformat()
f = open(f'/home/faem/dev/bots/selenium/udemy/{date}.txt','w')
for page in range (1,11):
    print(f'----------------Procesando página {page}----------------')
    url = f'https://www.udemy.com/courses/development/web-development/?p={page}&price=price-free&sort=popularity'
    browser.get(url)
    time.sleep(7)
    print('Extrayendo datos...')
    for i in range(1,18):
        if i != 4: #El <a> 4 no es del mismo tipo
            curso = str(i)
            name = browser.find_element_by_xpath(f'/html/body/div[2]/div[3]/div/div/div[6]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[{i}]/a/div/div[2]/div[1]').text
            link = browser.find_element_by_xpath(f'/html/body/div[2]/div[3]/div/div/div[6]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[{i}]/a')
            url = link.get_attribute("href")
            f.write(name+'\n')
            f.write(url+'\n')
            f.write('\n')
browser.close()
print('------------Extracción finalizada.---------------')
print(f'Archivo generado en: /home/faem/dev/bots/selenium/udemy/{date}.txt')

