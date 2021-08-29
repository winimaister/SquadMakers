
import time

from selenium import webdriver



dir = 'C:\\Users\\mros\\Downloads\\chromedriver_win32'
chrome_driver_path = dir + "\chromedriver.exe"
# crear sesion en chrome
driver = webdriver.Chrome(chrome_driver_path)



def openBrowser():
    login = 0
    # Configurar chromedriver

    driver.implicitly_wait(5)
    driver.maximize_window()

    # Abrir URL
    #driver.get("https://www.saucedemo.com/")
    driver.get("https://www.saucedemo.com/")
    #driver.execute_script('''window.open("","_blank");''')
    #driver.execute_script('''window.open("https://www.google.com","_blank");''')
    time.sleep(5)
    return driver

def closeBrowser():
    driver.close()


if __name__ == "__main__":
    openBrowser()