from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
chrome_driver_binary = '/Users/faem/dev/bots/selenium/drivers/macOS/chromedriver'
browser = webdriver.Chrome(executable_path=chrome_driver_binary,options=options)


url = "https://webventas.sofse.gob.ar/"
browser.get(url)
time.sleep(5)

ida_y_vuelta = browser.find_element_by_xpath('//*[@id="form_busqueda"]/div/div[2]/div[2]/div')
ida_y_vuelta.click()

origen = browser.find_element_by_xpath('//*[@id="origen-selectized"]')
origen.send_keys('Buenos Aires' + Keys.ENTER)

destino = browser.find_element_by_xpath('//*[@id="destino-selectized"]')
destino.send_keys('Córdoba' + Keys.ENTER)

ida = browser.find_element_by_xpath('//*[@id="form_busqueda"]/div/div[4]/div[1]/div[1]/a')
ida.click()