from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class Modelo:
    def __init__(self):
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
    
    def obtenerDriver(self):
        return self.driver