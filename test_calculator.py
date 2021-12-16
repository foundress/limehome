import unittest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service

import pathlib
import os


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        working_dir = pathlib.Path(__file__).parent.resolve()
        chromedriver_path = f"{working_dir}\\chromedriver"
        service = Service(chromedriver_path)
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.get(os.environ['CALCULATOR_URL'])

    def test_title(self):
        assert "Super Calculator" in self.driver.title

    def _set_input_value(self, model_name: str, element_value: str):
        input_field = self.driver.find_element(By.XPATH, f"//input[@ng-model='{model_name}']")
        input_field.clear()
        input_field.send_keys(element_value)

    def _set_operation(self, operation_value: str):
        self.driver.find_element(By.XPATH, "//select[@ng-model='operator']").click()
        self.driver.find_element(By.XPATH, f"//select[@ng-model='operator']//option[@value='{operation_value}']").click()

    def test_addition(self):
        self._set_input_value('first', '8')
        self._set_operation('ADDITION')
        self._set_input_value('second', '8')
        self.driver.find_element(By.ID, "gobutton").click()
        time.sleep(6)

        expected = 16
        actual = int(self.driver.find_element(By.CLASS_NAME, "ng-binding").text)
        assert expected == actual

    def test_history(self):
        # First operation
        self._set_input_value('first', '16')
        self._set_operation('DIVISION')
        self._set_input_value('second', '4')

        self.driver.find_element(By.ID, "gobutton").click()
        time.sleep(6)

        expected = 4
        actual = int(self.driver.find_element(By.CLASS_NAME, "ng-binding").text)
        assert expected == actual


        # Second operation
        self._set_input_value('first', '4')
        self._set_operation('MULTIPLICATION')
        self._set_input_value('second', '4')
        self.driver.find_element(By.ID, "gobutton").click()
        time.sleep(6)

        expected = 16
        actual = int(self.driver.find_element(By.CLASS_NAME, "ng-binding").text)
        assert expected == actual

        list = self.driver.find_elements(By.XPATH, "//table[@class='table']//tr[@ng-repeat='result in memory']")
        count = 0
        for elem in list:
            count = count + 1

        expected = 2
        actual = count
        assert expected == actual

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
