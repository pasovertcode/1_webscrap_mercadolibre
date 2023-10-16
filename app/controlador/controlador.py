from ..vista.vista import Navegador
from selenium.webdriver.common.by import By
import json
class Controlador:
    def __init__(self):
        self.vista = Navegador()
    
    def ejecutar(self):
        # url = input("Escriba la URL: ")
        arrayPath = self.obtenerPath()
        url = "https://www.mercadolibre.com.co/"
        self.vista.abrir_pagina(url)
        fieldBusqueda = self.vista.obtener_Elemento('input#cb1-edit')
        fieldBusqueda.send_keys(arrayPath['busqueda_producto'])
        self.vista.hacer_clic('button.nav-search-btn')
        listaProductos = []
        i = 0
        
        # Obtener todos las url de los productos 
        while True:
            i+=1
            c_p_almacenado = 0
            for elemento in self.vista.obtener_todos_Elementos('li.ui-search-layout__item'):
                nombre_producto = elemento.find_element(By.CSS_SELECTOR, 'h2.ui-search-item__title').text
                url_producto = elemento.find_element(By.CSS_SELECTOR, 'a.ui-search-link').get_attribute('href')
                precio_producto = int(elemento.find_element(By.CSS_SELECTOR, 'div.ui-search-price__second-line').text.split('\n')[1].replace(".", ""))
                listaProductos.append(
                    {
                        'nombre_producto': nombre_producto,
                        'url_producto': url_producto,
                        'precio_producto': precio_producto
                    }
                )
                c_p_almacenado+=1
                print(f"Producto: {nombre_producto} almacenado.")
            print(f"Cantidad de productos almacenados: {c_p_almacenado}")
            print(f"Cantidad total: {listaProductos.len()}")
            url_siguiente_pag = self.vista.obtener_Elemento("li.andes-pagination__button--next > a.andes-pagination__link").get_attribute('href')
            if url_siguiente_pag != None:
                self.vista.abrir_pagina(url_siguiente_pag)
            else:
                break

            if i == 1:
                break
        # Guardar pre-data de productos en un archivo .json en local
        pathFile = "app/resources/datos.json"
        with open(pathFile, "w") as archivo:
            json.dump(listaProductos, archivo)
        print(f"Datos guardados en: {pathFile}")



        
        espera = input()
        
        """ 
        for path in arrayPath:
            print(f"{path}: {self.vista.obtener_texto(arrayPath.get(path))}") 
        print("print del div: " + self.vista.obtener_texto(".ui-pdp-review__rating¿") )
        #  > div.ui-pdp-header__info
        titulo = self.vista.obtener_texto('h1.ui-pdp-title')
        print(f"Nombre Producto: {titulo}") """


    def busquedaProducto(self):
        pass
    def obtenerPath(self):
        path = {
            'busqueda_producto': "televisores smart tv",
            'nombre_producto': 'h1.ui-pdp-title',
            'calificacion_producto': 'span.ui-pdp-review__rating',
            'cantidad_calificadores': 'span.ui-pdp-review__amount',
            'precio_producto': 'span.andes-money-amount__fraction',
            'cantidad_disponible': 'span.ui-pdp-buybox__quantity__available'
            }
        return path
    