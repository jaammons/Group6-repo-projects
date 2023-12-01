from selenium import webdriver
from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import pytest
import time



class UserTests(StaticLiveServerTestCase):  
    fixtures = ["testusers.json"]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    
    def login_admin(self):
        """
        Returns a ChromeDriver logged in as Admin on index.html.
        """
        self.selenium.get(f"{self.live_server_url}/users/login")
        self.selenium.find_element(By.NAME, "username").send_keys("Admin")
        self.selenium.find_element(By.NAME, "password").send_keys("Admin")
        self.selenium.find_element(By.NAME, "login").click()
        

    def test_login(self):
        """
        Test verifies login_admin was successful by checking user greeting
        on index.html after log in attempt.
        Expected result: Admin is logged in.
        """
        self.selenium.get(f"{self.live_server_url}/users/login")
        time.sleep(2)
        self.selenium.find_element(By.NAME, "username").send_keys("Admin")
        self.selenium.find_element(By.NAME, "password").send_keys("Admin")
        time.sleep(2)
        self.selenium.find_element(By.NAME, "login").click()
        time.sleep(2)
        greeting = self.selenium.find_element(By.ID, "greeting")
        assert greeting.text == "Welcome, Admin."

    def test_logout(self):
        """
        Test verifies logout was successful by checking user greeting
        on index.html after log out attempt.
        Expected result: User is logged out.
        """
        self.login_admin()
        time.sleep(2)
        self.selenium.find_element(By.ID, "logout").click()
        time.sleep(2)
        greeting = self.selenium.find_element(By.ID, "greeting")
        assert greeting.text == "Not signed in."
    