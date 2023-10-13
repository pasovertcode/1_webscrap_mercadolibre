from ..vista.vista import Navegador
class Controlador:
    def __init__(self):
        self.vista = Navegador()
    
    def ejecutar(self):
        url = input("Digite URL: ")
        self.vista.abrir_pagina(url)