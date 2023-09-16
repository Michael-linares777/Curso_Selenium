from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# .explicit_wait(15) / Es un tiempo de espera... / para darle al navegador oportunidad de ejecutar si existen errores...
# Podes poner el tiempo que quieras....

driver = webdriver.Chrome()

driver.get("https://codigo369.com/frase-galleta")
driver.maximize_window()
time.sleep(6)

driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
driver.maximize_window()
t = 20

time.sleep(t)
driver.close()