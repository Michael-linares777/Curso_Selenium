from selenium import webdriver
import time

# NAVEGAR POR DIFERENTES PAGINAS....

t = 2

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(t)

driver.get("https://docs.python.org/3/")
driver.maximize_window()
time.sleep(t)

driver.get("https://codigo369.com/frase-galleta")
driver.maximize_window()
time.sleep(7)

# Para devolver una pagina... /  Navegar entre paginas /
# Tambien se puede usar .back() / pero es mejor usar el _script de javascript...

driver.execute_script("window.history.go(-1)")
time.sleep(t)

driver.execute_script("window.history.go(-1)")
time.sleep(t)

driver.close()

