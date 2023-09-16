from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# PRIMEROS PASOS CON LA FUNCIÓN KEYS...

# Inicializar el navegador...
driver = webdriver.Chrome()

# Abrir Pagina...
driver.get("https://www.google.com")

# Maximizar la pantalla...
driver.maximize_window()

# Buscar elementos por selector específico...
element = driver.find_element(By.XPATH,"//textarea[contains(@id,'APjFqb')]")
time.sleep(1)

# Pasar datos / info... al selector...
element.send_keys('Youtube')
time.sleep(1)

# Dar click en el selector...
element.send_keys(Keys.ENTER)
time.sleep(1)

# Cerrar el navegador...
driver.close()

