from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import pytest

def test_remember_me(driver):
    checkbox = driver.find_element(By.NAME, "remember_me")