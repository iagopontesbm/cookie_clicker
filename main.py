from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

TEMPO_EXECUTAR = 30
INTERVALO_COMPRA = 5

# Manter navegador aberto
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie")

cookie = driver.find_element(By.ID, value="cookie")
cursor = driver.find_element(By.ID, value="buyCursor")
grandma = driver.find_element(By.ID, value="buyGrandma")

tempo_inicio = time.time()
ultimo_comando = tempo_inicio

while (time.time() - tempo_inicio) < TEMPO_EXECUTAR:
    cookie.click()
    if (time.time() - ultimo_comando) >= INTERVALO_COMPRA:
        cursor.click()
        # grandma.click()
        ultimo_comando = time.time()
        print("Compra realizada!")

