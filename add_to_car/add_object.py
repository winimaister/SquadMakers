
from selenium.common.exceptions import NoSuchElementException
import time
from Browser import prueba
from selenium.webdriver.common.keys import Keys
from login.login import Login
#Nos logueamos utilizando el find element id del user y del password
from Browser.prueba import driver

objects = {
    0: "add-to-cart-sauce-labs-backpack",
    1: "add-to-cart-sauce-labs-bike-light",
    2: "add-to-cart-test.allthethings()-t-shirt-(red)"
}
car_page=4 #variable para indicar el link text correspondiente a la pagina del carrito

#mediante bucle seleccionamos todos los objetos que queremos añadir al carrito  previamente asociados a una array para
#en un futuro añadir mas si se desea
def add():
    global objects
    num_objects=len(objects)
    for x in range(num_objects):
        driver.find_element_by_id(objects[x]).click()

def open_car():
    driver.find_element_by_xpath("//div[@id='shopping_cart_container']/a").click()
    if driver.current_url=="https://www.saucedemo.com/cart.html":
        #assert driver
        pass
    driver.find_element_by_id("checkout").click()

def buy():
    campo_Name = driver.find_element_by_id("first-name")
    # borramos por si llegara existir al gun caracter y asi tener el campo vacio
    campo_Name.clear()
    campo_Name.send_keys("Miguel")
    campo_LastName = driver.find_element_by_id("last-name")
    # borramos por si llegara existir al gun caracter y asi tener el campo vacio
    campo_LastName.clear()
    campo_LastName.send_keys("Ros")
    campo_code = driver.find_element_by_id("postal-code")
    # borramos por si llegara existir al gun caracter y asi tener el campo vacio
    campo_code.clear()
    campo_code.send_keys("12345")

    driver.find_element_by_id("continue").click()

    if driver.current_url=="https://www.saucedemo.com/checkout-step-two.html":
        if "CHECKOUT: OVERVIEW" in driver.page_source:
            pass


    driver.find_element_by_id("finish").click()
    if driver.current_url == "https://www.saucedemo.com/checkout-complete.html":

        if "THANK YOU FOR YOUR ORDER" in driver.page_source:
            Test=1
            pass
    return Test


def test_buy():
    Login()
    add()
    open_car()
    buy()

if __name__ == "__main__":
    Login()
    add()
    open_car()
    buy()