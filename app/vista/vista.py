from ..modelo.modelo import Modelo
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urllib.parse import urlparse

class Navegador:
    def __init__(self):
        self.driver = Modelo().obtenerDriver()

    def obtener_actual_URL(self):
        return self.driver.current_url

    def abrir_pagina(self, url_page):
        self.driver.get(url_page)

    def hacer_clic(self, selector):
        boton = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        boton.click()

    def obtener_texto(self, selector):
        try:

            elemento = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))

            return elemento.text
        except Exception as e:
            print (f"Se ha producido una excepción: {e}")
        finally:
            return '0'
        
    def obtener_Elemento(self, selector):
        try:

            elemento = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))

            return elemento
        except Exception as e:
            return f"Se ha producido una excepción: {e}"
    def obtener_todos_Elementos(self, selector):
        try:

            elementos = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, selector)))

            return elementos
        except Exception as e:
            return f"Se ha producido una excepción: {e}"
        
    def obtener_todos_Elementos_no_Visibles(self, selector):
        try:

            elementos = self.driver.find_elements(By.CSS_SELECTOR, selector)

            return elementos
        except Exception as e:
            return f"Se ha producido una excepción: {e}"