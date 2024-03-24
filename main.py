from selenium import webdriver
from selenium.webdriver.common.by import By
import time

TEMPO_EXECUTAR = 30  # 300 segundos
INTERVALO_COMPRA = 5  # 5 segundos

# Manter navegador aberto
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie")

cookie = driver.find_element(By.ID, value="cookie")


def money():
    """Retorna o valor de gold"""
    m = int(driver.find_element(By.ID, value="money").text.replace(",", ""))
    return m


def store_values():
    """Retorno um dicionário com o valor de cada item na loja"""
    st_values = {}
    values = driver.find_elements(By.CSS_SELECTOR, value="#rightPanel b")
    for v in values[:8]:
        name, vl = v.text.split(" - ")
        st_values[name] = int(vl.replace(",", ""))
    return st_values


# Variaveis iniciais de tempo
tempo_inicio = time.time()
ultimo_comando = tempo_inicio

while (time.time() - tempo_inicio) < TEMPO_EXECUTAR:
    cookie.click()  # Clique no biscoito
    if (time.time() - ultimo_comando) >= INTERVALO_COMPRA:
        store = driver.find_element(By.ID, value="store")
        money_value, store_itens = money(), store_values()  # Armazena os valores das funções
        max_value = float('-inf')
        max_key = None
        # Loop para verificar o maior valor nos itens da loja que seja menor que o gold atual
        for key, value in store_itens.items():
            if money_value > value > max_value:
                max_key = key
                max_value = value
        item_select = store.find_element(By.CSS_SELECTOR, value=f'[onclick="Buy(\'{max_key}\');"]')
        item_select.click()  # Clique no item selecionado da loja
        ultimo_comando = time.time()

cookie_sec = driver.find_element(By.ID, value="cps")
print(cookie_sec.text)
