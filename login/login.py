from selenium.common.exceptions import NoSuchElementException
import time
from Browser import prueba
from Browser.prueba import driver
from selenium.webdriver.common.keys import Keys

#Nos logueamos utilizando el find element id del user y del password


def Login():
    prueba.openBrowser()
    #Escribir Mail
    campo_Mail=prueba.driver.find_element_by_id("user-name")
    #borramos por si llegara existir al gun caracter y asi tener el campo vacio
    campo_Mail.clear()
    campo_Mail.send_keys("standard_user")

    #Escribir Pass
    campo_Pass=prueba.driver.find_element_by_id("password")
    # borramos por si llegara existir al gun caracter y asi tener el campo vacio
    campo_Pass.clear()
    campo_Pass.send_keys("secret_sauce")

    campo_Pass.submit()
    time.sleep(3)
    #LoginTrue()
    time.sleep(3)

#comprobacion de que se ha realizado el Login correctamente

def LoginTrue():
    try:
        if driver.current_url == "https://www.saucedemo.com/inventory.html":
            print("Login correcto, test pasado")
            log_correct=1
        else:
            log_correct = 0
            print("No se ha logueado")
    except NoSuchElementException:
        print("No existe")

    if log_correct==1:
        test=1
    else:
        test=0



if __name__ == "__main__":
    Login()
    LoginTrue()