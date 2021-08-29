from selenium.common.exceptions import NoSuchElementException
import time
from Browser import prueba
from Browser.prueba import driver
from selenium.webdriver.common.keys import Keys

import login

def logout():
    Test = 0
    #busco el menu desplegable y lo abro
    driver.find_element_by_id("react-burger-menu-btn").click()
    #busco la ubicacion del Logout y clico
    driver.find_element_by_id("logout_sidebar_link").click()

    #compruebo que la pagina actual sea la de Login
    if driver.current_url == "https://www.saucedemo.com/":

        if "LOGIN" in driver.page_source:
            Test = 1
            pass

        return Test


def test_logout():
    login.Login()
    logout()


if __name__ == "__main__":
    login.Login()
    logout()