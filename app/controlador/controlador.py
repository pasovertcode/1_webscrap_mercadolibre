from ..vista.vista import Navegador
from selenium.webdriver.common.by import By
import json
class Controlador:
    def __init__(self):
        self.vista = Navegador()
    
    def ejecutar(self):
        # url = input("Escriba la URL: ")
        busqueda_producto = "televisores smart tv"
        arrayPath = self.obtenerPath()
        url = "https://www.mercadolibre.com.co/"
        self.vista.abrir_pagina(url)
        fieldBusqueda = self.vista.obtener_Elemento('input#cb1-edit')
        fieldBusqueda.send_keys(busqueda_producto)
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
            print(f"Cantidad de productos almacenados: {c_p_almacenado} en la pagina: {i}" )
            print(f"Cantidad total: {len(listaProductos)}")
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

        # Navegar a cada producto y obtener data
        lista_data_productos = []
        for producto in listaProductos:
            self.vista.abrir_pagina(producto['url_producto']) 
            dict_productos = arrayPath.copy()
            for path in arrayPath:
                dict_productos[path] = self.vista.obtener_texto(arrayPath.get(path))
                print(f"{path}: {self.vista.obtener_texto(arrayPath.get(path))}")
            
            
            lista_nodos = self.vista.obtener_todos_Elementos_no_Visibles('.ui-vpp-striped-specs__table')

            for nodo in lista_nodos:
                
                if "Características generales" == nodo.find_element(By.CSS_SELECTOR,'h3').get_attribute('innerHTML') :
                    for tablerow in nodo.find_elements(By.CSS_SELECTOR,"tr.andes-table__row"):
                        print("Características encontradas.")
                        if "Marca" == tablerow.find_element(By.CSS_SELECTOR,"div.andes-table__header__container").get_attribute('innerHTML'):
                            dict_productos["Marca"] = tablerow.find_element(By.CSS_SELECTOR,"span.andes-table__column--value").get_attribute('innerHTML')
                        if "Línea" == tablerow.find_element(By.CSS_SELECTOR,"div.andes-table__header__container").get_attribute('innerHTML'):
                            dict_productos["Línea"] = tablerow.find_element(By.CSS_SELECTOR,"span.andes-table__column--value").get_attribute('innerHTML')
                        if "Modelo" == tablerow.find_element(By.CSS_SELECTOR,"div.andes-table__header__container").get_attribute('innerHTML'):
                            dict_productos["Modelo"] = tablerow.find_element(By.CSS_SELECTOR,"span.andes-table__column--value").get_attribute('innerHTML')
                        if "Color" == tablerow.find_element(By.CSS_SELECTOR,"div.andes-table__header__container").get_attribute('innerHTML'):
                            dict_productos["Color"] = tablerow.find_element(By.CSS_SELECTOR,"span.andes-table__column--value").get_attribute('innerHTML')
                if "Pantalla" == nodo.find_element(By.CSS_SELECTOR,'h3').get_attribute('innerHTML') :
                    for tablerow in nodo.find_elements(By.CSS_SELECTOR,"tr.andes-table__row"):
                        if "Tipo de pantalla" == tablerow.find_element(By.CSS_SELECTOR,"div.andes-table__header__container").get_attribute('innerHTML'):
                            dict_productos["tipo_pantalla"] = tablerow.find_element(By.CSS_SELECTOR,"span.andes-table__column--value").get_attribute('innerHTML')

            print(f"Nuevo producto agregado. info: {dict_productos}")   
            lista_data_productos.append(dict_productos)              
        
        espera = input()
        


    def busquedaProducto(self):
        pass
    def obtenerPath(self):
        path = {
            'nombre_producto': 'h1.ui-pdp-title',
            'precio_producto': 'span.andes-money-amount__fraction',
            'cantidad_disponible': 'span.ui-pdp-buybox__quantity__available'
            }
        return path
    