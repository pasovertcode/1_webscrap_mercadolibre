from ..modelo.modelo import Modelo
class Navegador:
    def __init__(self):
        self.driver = Modelo().obtenerDriver()

    def obtener_actual_URL(self):
        return self.driver.current_url

    def abrir_pagina(self, url_page):
        self.driver.get(url_page)