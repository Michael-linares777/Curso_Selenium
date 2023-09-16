from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializar el navegador...
driver = webdriver.Chrome()

# Abrir Google...
driver.get("https://www.google.com")

# Maximizar la pantalla...
driver.maximize_window()
time.sleep(1)

# Buscar elementos por selector específico...
element = driver.find_element(By.XPATH,"//textarea[contains(@id,'APjFqb')]")
element.send_keys('Udemy')
time.sleep(1)

element.send_keys(Keys.ENTER)
time.sleep(1)

# Para automatizar el desplazamiento hacia abajo / Con un sistema de scroll de JavaScrip...
driver.execute_script("window.scrollTo(0, 400)")
time.sleep(1)

# Cerrar el navegador...
driver.quit()

print('Fin...')
