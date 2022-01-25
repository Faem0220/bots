from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from random import randint
filepath = 'whatsapp_session.txt'
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        if cnt == 0:
            executor_url = line
        if cnt == 1:
            session_id = line

def create_driver_session(session_id, executor_url):
    from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

    org_command_execute = RemoteWebDriver.execute

    def new_command_execute(self, command, params=None):
        if command == "newSession":
            # Mock the response
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return org_command_execute(self, command, params)

    RemoteWebDriver.execute = new_command_execute

    new_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    new_driver.session_id = session_id

    RemoteWebDriver.execute = org_command_execute

    return new_driver



driver2 = create_driver_session(session_id, executor_url)
print("Driver 2 URL: " + driver2.current_url)

# A dictionary that stores all the users with permissions to activate bot
bot_users = {
    "USERS": True,
   
}

# A dictionary of unauthorized and banned users
unauthorized_bot_users = {}
message_count = 0
while True:
    wait = WebDriverWait(driver2, 600)
    # Green dot for new messages---> Bug if conversation is already open.
    unread = driver2.find_elements_by_class_name("_23LrM")
    name, message = '', ''
    if len(unread) > 0:
        ele = unread[-1]
        action = webdriver.common.action_chains.ActionChains(driver2)
        action.move_to_element_with_offset(ele, 0, -20)  # move a bit to the left from the green dot
        # Clicking couple of times because sometimes whatsapp web responds after two clicks
        try:
            action.click()
            action.perform()
            action.click()
            action.perform()
        except Exception as e:
            pass
        try:
            # Contact name
            name = driver2.find_element_by_class_name("_2rlF7").text
            print(name)
            # Last Message in chat
            message = driver2.find_elements_by_class_name("_1Gy50")[-1].text
            print(message)

            
            if name in bot_users:
                if message.lower() == 'activar':
                    bot_users[name] = True
                if bot_users[name]:
                    if message.lower() == 'acciones':
                        text_box = driver2.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div')
                        response = "Hola " + name + "!\n"\
                                            " El modo bot está activado\n" \
                                            "En qué puedo ayudarte:\n" \
                                            "-Para invertir texto escribe: espejo=texto \n" \
                                            "-Para contar los caracteres de un texto escribe: contar=texto \n" \
                                            "-Para buscar un sonido aleatorio escribe: sonido \n" \
                                            "-Para desactivar el bot escribe: Desactivar\n"             
                        text_box.send_keys(response + Keys.RETURN)
                        continue
                    if message.lower().startswith('espejo='):
                        text_box = driver2.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div')
                        response = ''.join(reversed(message[7:]))
                        text_box.send_keys(response + Keys.RETURN)
                        continue

                    if message.lower().startswith('contar='):
                        text_box = driver2.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div')
                        response = str(len(message[7:].replace(' ','')))
                        text_box.send_keys(response + Keys.RETURN)
                        continue
                    if message.lower().startswith('sonido'):
                        num = randint(1000,2400)
                        text_box = driver2.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div')
                        response = f'https://bigsoundbank.com/detail-{num}.html'
                        text_box.send_keys(response + Keys.RETURN)
                        continue
                    
                    if message.lower() == 'desactivar':
                        text_box = driver2.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div')
                        response = ('Adios '+name+'. Vuelva prontos. Cuando quieras volver escribe: activar')
                        text_box.send_keys(response + Keys.RETURN)
                        bot_users[name] = False
                    
                    if message.lower().startswith('sortear='):
                        text_box = driver2.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div')
                        response = sorted(message)
                        text_box.send_keys(response + Keys.RETURN)
                        continue
            

                    else:
                        text_box = driver2.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div')
                        response = "No entiendo qué quieres decir.\n"\
                                    "Para ver qué puedo hacer escribe: acciones"
                        text_box.send_keys(response + Keys.RETURN)
                else:
                    message_count += 1
                    if message_count == 3:
                        text_box = driver2.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div')
                        response = "----Modo bot desactivado.----\n"\
                                    " Para activar escribe: activar"
                        text_box.send_keys(response + Keys.RETURN)
                        message_count = 0
            else:
                print(name,' no está autorizado')
            
            
        except Exception as e:
            print('DEBUG',e)
            pass
    else:
        #ESTA OPCION ES POR SI CAMBIAN LOS ELEMENTOS HTML
        driver2.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/div[2]/div[1]/div/div/div[3]/div/div/div[2]/div[1]/div[1]/span').click()
        
    sleep(5)

            




    



        
    
