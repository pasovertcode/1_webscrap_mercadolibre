from ..vista.vista import Navegador
from selenium.webdriver.common.by import By
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
        auxLista = []
        while True:
            
            listaProductos = self.vista.obtener_todos_Elementos('li.ui-search-layout__item')
            for elemento in listaProductos:
                auxLista.append(
                    {
                        'nombre_producto': elemento.find_element(By.CSS_SELECTOR, 'h2.ui-search-item__title').text,
                        'url_producto': elemento.find_element(By.CSS_SELECTOR, 'a.ui-search-link').get_attribute('href'),
                        'precio_producto': int(elemento.find_element(By.CSS_SELECTOR, 'div.ui-search-price__second-line').text.split('\n')[1].replace(".", ""))
                    }
                )
            
            url_siguiente_pag = self.vista.obtener_Elemento("li.andes-pagination__button--next > a.andes-pagination__link").get_attribute('href')
            print(f"Url de la nav siguiente: {url_siguiente_pag}")
            print(auxLista[0])
            if url_siguiente_pag != None:
                self.vista.abrir_pagina(url_siguiente_pag)
            else:
                break
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
    