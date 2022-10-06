# Crear 20 empleados
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import names
import random
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'C:/Users/Maynar/Desktop/pythonProject/.env')
load_dotenv(dotenv_path)

# Environment Variables
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
BASE_URL = os.getenv('URL')


class Home:

    # -- Locators --
    def __init__(self, driver):
        self.driver = driver
        self.user = 'Usuario'
        self.password = 'Password'
        self.btn_ingresar = 'btnIngresar'
        self.administracion = '/html/body/main/aside/section/nav/ul/li[2]/div/label'
        self.empleados = '/html/body/main/aside/section/nav/ul/li[2]/div/div/ul/li[2]/a'
        self.btn_add = '//*[@id="Empleados"]/div/div[1]/button'
        self.inpt_name = '//*[@id="Nombre"]'
        self.inpt_surname = '//*[@id="Apellido"]'
        self.dni = '//*[@id="DNI"]'
        self.save_changes = '//*[@id="modalNuevoEmpleado"]/div[2]/div/div[3]/button[2]'
        self.entendido = '//*[@id="modal-procesar-respuesta"]/div[2]/div/div[3]/button'
        self.msg_error = '//*[@id="modal-procesar-respuesta"]/div[2]/div/div[2]/label'


    # -- Get Elements --
    def get_user(self):
        return self.driver.find_element(By.ID, self.user)

    def get_password(self):
        return self.driver.find_element(By.ID, self.password)

    def get_btn_ingresar(self):
        return self.driver.find_element(By.ID, self.btn_ingresar)

    def get_administracion(self):
        return self.driver.find_element(By.XPATH, self.administracion)

    def get_empleados(self):
        return self.driver.find_element(By.XPATH, self.empleados)

    def get_btn_add(self):
        return self.driver.find_element(By.XPATH, self.btn_add)

    def get_inpt_name(self):
        return self.driver.find_element(By.XPATH, self.inpt_name)

    def get_inpt_surname(self):
        return self.driver.find_element(By.XPATH, self.inpt_surname)

    def get_dni(self):
        return self.driver.find_element(By.XPATH, self.dni)

    def get_btn_save_changes(self):
        return self.driver.find_element(By.XPATH, self.save_changes)

    def get_entendido(self):
        return self.driver.find_element(By.XPATH, self.entendido)

    def get_msg_error(self):
        return self.driver.find_element(By.XPATH, self.msg_error)

    # -- Actions --
    def gen_employ(self):
        # Generar 20 empleados en loop
        # El registro solo se anula en localhost
        x = range(30)
        for n in x:
            print(n)
            self.driver.get(BASE_URL)
            self.get_user().send_keys(USER)
            self.get_password().send_keys(PASSWORD)
            self.get_btn_ingresar().click()
            time.sleep(3)
            self.get_administracion().click()
            self.get_empleados().click()
            time.sleep(5)
            self.get_btn_add().click()
            time.sleep(5)
            # Data Employee
            self.get_inpt_name().send_keys(names.get_first_name())
            self.get_inpt_surname().send_keys(names.get_last_name())
            self.get_dni().send_keys(str(random.randint(20000000, 40000000)))
            self.get_btn_save_changes().click()
            time.sleep(3)
            self.get_entendido().click()

        time.sleep(4)

        msg_error = self.get_msg_error().text

        assert msg_error == 'Superó la cantidad de legajos permitidos!'



