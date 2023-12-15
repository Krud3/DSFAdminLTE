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
    text_1 = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/section/div/div/section[2]/form/div[1]/div/div/div[2]/div[1]/input")
    text_2 = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/section/div/div/section[2]/form/div[1]/div/div/div[2]/div[2]/select")
    text_3 = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/section/div/div/section[2]/form/div[1]/div/div/div[2]/div[3]/input")
    text_4 = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/section/div/div/section[2]/form/div[1]/div/div/div[2]/div[4]/input")
    text_5 = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/section/div/div/section[2]/form/div[1]/div/div/div[2]/div[5]/input")

    text_1.send_keys("SUCPRUEBA{indice}")
    text_2.send_keys("2")
    text_3.send_keys("SUCU{indidce}")
    text_4.send_keys("ciudad{indidce}")
    text_5.send_keys("tel{indidce}")
    driver.save_screenshot(f'prueba_crearSucuAntes_{indice}.png')
    submit_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/section/div/div/section[2]/form/div[2]/div/input")
    time.sleep(2)
    submit_button.click()
    driver.save_screenshot(f'prueba_crearSucuDespues_{indice}.png')

    # Pausa para que la página se actualice
    time.sleep(2)

    # Tomar y guardar una captura de pantalla
    

# Realizar las pruebas
url2 = "http://localhost:8000/adminlte/add_sucursal/"
login(credencial)
for i in range(0, 5):
    navegar(url2, i)

# Cerrar el navegador
driver.quit()
