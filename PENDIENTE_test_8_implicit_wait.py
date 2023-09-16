from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# .implicit_wait(15) / Es un tiempo de espera... / para darle al navegador oportunidad de ejecutar si existen errores...
# Podes poner el tiempo que quieras....

driver = webdriver.Chrome()

driver.get("https://codigo369.com/frase-galleta")
driver.maximize_window()
time.sleep(7)

driver.get("")
driver.maximize_window()
driver.implicitly_wait(15)

t = 1

time.sleep(t)
driver.close()