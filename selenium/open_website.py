from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
chrome_driver_binary = '/Users/faem/dev/bots/selenium/drivers/macOS/chromedriver'
browser = webdriver.Chrome(executable_path=chrome_driver_binary,options=options)

url = "https://google.com"
browser.get(url)
