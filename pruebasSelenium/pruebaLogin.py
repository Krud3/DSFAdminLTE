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
credenciales = [
    {"username": "GER0001", "password": "12345"},
    {"username": "usuario1", "password": "clave1"},
    {"username": "usuario2", "password": "clave2"},
    {"username": "usuario3", "password": "clave3"},
    {"username": "usuario4", "password": "clave4"}
]

# Función para realizar un intento de inicio de sesión y tomar una captura de pantalla
def realizar_prueba(credencial, prueba_numero):
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
    driver.save_screenshot(f'prueba_{prueba_numero}.png')

# Realizar las pruebas
for i, credencial in enumerate(credenciales):
    realizar_prueba(credencial, i + 1)

# Cerrar el navegador
driver.quit()
