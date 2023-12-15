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
listaEste = ['0001', '0002','0003','0004']
lista_id = {'http://localhost:8000/adminlte/agregar_sucursal/', 'http://localhost:8000/adminlte/agregar_sucursal/','http://localhost:8000/adminlte/agregar_sucursal/','http://localhost:8000/adminlte/agregar_sucursal/'}

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
    buscador = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/section/div/section/div/div/input")
    buscador.send_keys(listaEste[indice])

    # Pausa para que la página se actualice
    time.sleep(2)

    # Tomar y guardar una captura de pantalla
    driver.save_screenshot(f'prueba_buscarSucursal_{indice}.png')

# Realizar las pruebas
url2 = "http://localhost:8000/adminlte/agregar_sucursal/"
login(credencial)
for i in range(0, 4):
    navegar(url2, i)

# Cerrar el navegador
driver.quit()
