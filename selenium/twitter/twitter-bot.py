from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time
from getpass import getpass

browser = webdriver.Firefox(executable_path='/home/faem/dev/bots/selenium/geckodriver')
def sign_in_twitter():
    
    browser.get("https://www.twitter.com/login")
    time.sleep(5)
    usernameInput = browser.find_element_by_name("session[username_or_email]")
    passwordInput = browser.find_element_by_name("session[password]")
    usernameInput.send_keys('__faem__')
    password = getpass()
    passwordInput.send_keys(password)
    passwordInput.send_keys(Keys.ENTER)
    time.sleep(5)

def tweet_something():
    tweet = browser.find_element_by_xpath('''/html/body/div/div/div/div[2]
                                            /main/div/div/div/div[1]/div/div[2]
                                            /div/div[2]/div[1]/div/div/div/div[2]
                                            /div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div''')
    tweet.click()
    tweet.send_keys('.......')
    tweet.send_keys(Keys.CONTROL, Keys.ENTER)

sign_in_twitter()
tweet_something()

