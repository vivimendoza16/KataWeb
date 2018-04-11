__author__ = 'asistente'
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('C:\\Users\\vcmb1\\chromedriver.exe')

    def tearDown(self):
        self.browser.quit()
    """
    def test_title(self):
        self.browser.get('http://www.google.com.co')
        self.assertIn('Google', self.browser.title)
    """
    """
    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)
    """
    """
    def test_registro(self):
        self.browser.get('http://localhost:8000')
        self.browser.implicitly_wait(1000)
        link = self.browser.find_element_by_id('id_register')
        self.browser.implicitly_wait(1000)
        link.click()

        self.browser.implicitly_wait(1000)
        nombre = self.browser.find_element_by_id('id_nombre')
        self.browser.implicitly_wait(1000)
        nombre.send_keys('Juan Sebastian')
        self.browser.implicitly_wait(1000)

        apellidos = self.browser.find_element_by_id('id_apellidos')
        self.browser.implicitly_wait(1000)
        apellidos.send_keys('Hernandez')
        self.browser.implicitly_wait(1000)

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        self.browser.implicitly_wait(1000)
        experiencia.send_keys('5')
        self.browser.implicitly_wait(1000)

        self.browser.find_element_by_xpath("//select[@id='id_tiposDeServicio']/option[text()='Jardineria']").click()
        self.browser.implicitly_wait(1000)
        telefono = self.browser.find_element_by_id('id_telefono')
        self.browser.implicitly_wait(1000)
        telefono.send_keys('3173024578')
        self.browser.implicitly_wait(1000)

        correo = self.browser.find_element_by_id('id_correo')
        self.browser.implicitly_wait(1000)
        correo.send_keys('js.hernandez1@uniandes.edu.co')
        self.browser.implicitly_wait(1000)

        imagen = self.browser.find_element_by_id('id_imagen')
        self.browser.implicitly_wait(1000)
        imagen.send_keys('C:\\Users\\vcmb1\\Desktop\\Jardineria.jpg')
        self.browser.implicitly_wait(1000)

        nombreUsuario = self.browser.find_element_by_id('id_username')
        self.browser.implicitly_wait(1000)
        nombreUsuario.send_keys('juans')
        self.browser.implicitly_wait(1000)

        clave = self.browser.find_element_by_id('id_password')
        self.browser.implicitly_wait(1000)
        clave.send_keys('clave123')
        self.browser.implicitly_wait(8000)

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        self.browser.implicitly_wait(1000)
        botonGrabar.click()
        self.browser.implicitly_wait(1000)
        span=self.browser.find_element(By.XPATH, '//span[text()="Juan Sebastian Hernandez"]')
        self.browser.implicitly_wait(1000)

        self.assertIn('Juan Sebastian Hernandez', span.text)
    """
    """
    def test_verDetalle(self):
        self.browser.get('http://localhost:8000')
        span=self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        span.click()
        self.browser.implicitly_wait(1000)
        h2=self.browser.find_element(By.XPATH, '//h2[text()="Juan Daniel Arevalo"]')
        self.browser.implicitly_wait(1000)
        self.assertIn('Juan Daniel Arevalo', h2.text)
    """

    def test_login(self):
        self.browser.get('http://localhost:8000')
        self.browser.implicitly_wait(500)
        link = self.browser.find_element_by_id('id_login')
        link.click()

        username=self.browser.find_element_by_id('id_username')
        username.send_keys('carlos')

        password = self.browser.find_element_by_id('id_password')
        password.send_keys('12345678')

        botonIngresar = self.browser.find_element_by_id('id_ingresar')
        botonIngresar.click()
        self.assertIn('Busco Ayuda', self.browser.title)



    def test_RegistrarComentario(self):
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        span.click()
        self.browser.implicitly_wait(1000)
        h2 = self.browser.find_element(By.XPATH, '//h2[text()="Juan Daniel Arevalo"]')
        self.browser.implicitly_wait(1000)
        comentario = self.browser.find_element_by_id('comentario')
        self.browser.implicitly_wait(1000)
        comentario.send_keys('Hola')
        correo = self.browser.find_element_by_id('correo')
        self.browser.implicitly_wait(1000)
        correo.send_keys('prueba@pureba.prueba')
        botonComent = self.browser.find_element_by_id('coment')
        self.browser.implicitly_wait(1000)
        botonComent.click()
        h2 = self.browser.find_element(By.XPATH, '//h2[text()="Juan Daniel Arevalo"]')
        self.browser.implicitly_wait(1000)
        self.assertIn('Juan Daniel Arevalo', h2.text)


    def test_editar(self):
        self.browser.get('http://localhost:8000/editar/19')
        ##self.browser.implicitly_wait(1000)

        self.browser.find_element_by_xpath("//select[@id='id_tiposDeServicio']/option[text()='Jardineria']").click()
        ##self.browser.implicitly_wait(1000)

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        ##self.browser.implicitly_wait(1000)
        botonGrabar.click()
        ##self.browser.implicitly_wait(1000)
        self.assertIn('Busco Ayuda', self.browser.title)

