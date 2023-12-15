from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurar Selenium para usar Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL del sitio de login
url = "http://localhost:8000/"

# Lista de credenciales para probar
credencial =  {"username": "GER0001", "password": "123facil123"}

lista_id = {'http://localhost:8000/adminlte/add_automovil/', 'http://localhost:8000/adminlte/add_jefe_taller/','http://localhost:8000/adminlte/gra_autos/','http://localhost:8000/adminlte/agregar_repuesto/'}

# Función para realizar un intento de inicio de sesión y tomar una captura de pantalla
def login(credencial):
    # Abrir la URL con Selenium
    driver.get(url)

    # Encontrar el campo de usuario y contraseña e ingresar los datos
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")

    username.clear()
    password.clear()

    username.send_keys(credencial["username"])
    password.send_keys(credencial["password"])

    # Enviar el formulario
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # Pausa para que la página se actualice
    time.sleep(2)

    # Tomar y guardar una captura de pantalla
    #driver.save_screenshot(f'prueba_{prueba_numero}.png')

def navegar( url,indice):
    # Enviar el formulario
    driver.get(url)
    #submit_button = driver.find_element(By.ID, lista_id[prueba_numero])
    #submit_button.click()

    # Pausa para que la página se actualice
    time.sleep(2)

    # Tomar y guardar una captura de pantalla
    driver.save_screenshot(f'prueba_navegar_{indice}.png')

# Realizar las pruebas
driver.get(url)
for indice, urls in enumerate(lista_id):
    navegar(urls, indice)

# Cerrar el navegador
driver.quit()
