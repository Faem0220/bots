from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

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
    "USER": True,
}

# A dictionary that stores those users that the bot already indicated them how to activate it
bot_users_notification = {
    "USER": False,
    
}

# A dictionary of unauthorized and banned users
unauthorized_bot_users = {}

while True:
    wait = WebDriverWait(driver2, 600)
    # Green dot for new messages
    unread = driver2.find_elements_by_class_name("_1pJ9J")
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
            name = driver2.find_element_by_class_name("_2rlF7")
            print(name.text)
            # Instructions for out bot
            message = driver2.find_elements_by_class_name("_1Gy50")[-1]
            print(message.text)
            if name.text in bot_users:
                if bot_users[name.text]:
                    if '1' == message.text:
                        text_box = driver2.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div')
                        response = 'Escribe el presupuesto máximo:'
                        text_box.send_keys(response + Keys.RETURN)
                        continue
                    if 'activar' == message.text.lower():
                        if name.text.lower() not in bot_users:
                            text_box = driver2.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div')
                            bot_users[name] = True
                            response = "Hi " + name.text + " faBot está activado\n" \
                                                           "En qué puedo ayudarte:\n" \
                                                           "1. Lista de casas \n" \
                                                           "2. Lista de deptos\n" \
                                                           "Desactivar\n" 
                            text_box.send_keys(response)
                            continue
                    if 'desactivar' == message.text.lower():
                        if name.text in bot_users:
                            if bot_users[name.text]:
                                text_box = driver2.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div')
                                response = "Adios " + name.text + ".\n"
                                text_box.send_keys(response)
                                bot_users[name.text] = None
                                bot_users_notification[name.text] = None
                    else:
                        text_box = driver2.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div')
                        response = "Opción no válida. Para ver las opciones escribe: Activar "
                        text_box.send_keys(response + Keys.RETURN)
                        bot_users_notification[name.text] = True
                else:
                    if not bot_users_notification[name.text]:
                        text_box = driver2.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div')
                        response = "Hola, para chatear con faBot escribe: Activar "
                        text_box.send_keys(response + Keys.RETURN)
                        bot_users_notification[name.text] = True
            else:
                print(name.text,' no está autorizado')
                if name.text not in unauthorized_bot_users:
                    unauthorized_bot_users[name.text] = True
                    # response = "Unauthorized User:" + name.text + ".\n"
        except Exception as e:
            print('DEBUG',e)
            pass
    else:
        #ESTA OPCION ES POR SI CAMBIAN LOS ELEMENTOS HTML 
        print('No hay mensajes nuevos')
    sleep(5)