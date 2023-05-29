import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class InvestmentPortfolio(unittest.TestCase):

    def setUp(self):
        self.driverdriver = webdriver.Chrome()

    def test_response(self):
        response = self.get("https://starfish-app-lzwkc.ondigitalocean.app/")
        self.assertEqual(response.status_code, 200)

    def test_buy_an_action(self): 
        driver = self.driver
        driver.get("https://starfish-app-lzwkc.ondigitalocean.app/")

        input("patch to prevent webdriver from crashing")
        self.assertIn("Mis inversiones", driver.title)

        element = driver.find_element_by_name("Aluar")

        element2 = driver.find_element_by_name("Comprar")

        element2.send_keys("1")

        element_button = driver.find_element_by_name("Realizar compra")

        response = self.get("https://starfish-app-lzwkc.ondigitalocean.app/")
        self.assertEqual(response.status_code, 201)

    def test_buy_a_negative_number_of_actions(self): 
        driver = self.driver
        driver.get("https://starfish-app-lzwkc.ondigitalocean.app/")

        input("patch to prevent webdriver from crashing")
        self.assertIn("Mis inversiones", driver.title)

        element = driver.find_element_by_name("Aluar")

        element2 = driver.find_element_by_name("Comprar")

        element2.send_keys("-1")

        element_button = driver.find_element_by_name("Realizar compra")

        response = self.get("https://starfish-app-lzwkc.ondigitalocean.app/")
        self.assertEqual(response.status_code, 400)
         
    def sell_an_action(self):
        driver = self.driver
        driver.get("https://starfish-app-lzwkc.ondigitalocean.app/")

        input("patch to prevent webdriver from crashing")

        element = driver.find_element_by_name("Aluar")

        element2 = driver.find_element_by_name("Vender")

        element2.send_keys("1")

        element_button = driver.find_element_by_name("Realizar venta")

        response = self.get("https://starfish-app-lzwkc.ondigitalocean.app/")
        self.assertEqual(response.status_code, 201)

    def sell_a_negative_number_of_actions(self):
        driver = self.driver
        driver.get("https://starfish-app-lzwkc.ondigitalocean.app/")

        input("patch to prevent webdriver from crashing")

        element = driver.find_element_by_name("Aluar")

        element2 = driver.find_element_by_name("Vender")

        element2.send_keys("-1")

        element_button = driver.find_element_by_name("Realizar venta")

        response = self.get("https://starfish-app-lzwkc.ondigitalocean.app/")
        self.assertEqual(response.status_code, 400)