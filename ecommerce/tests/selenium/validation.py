from selenium import webdriver
from selenium.webdriver.common.by import By

def validate_page_title(driver, title):
    if title in driver.title:
        return True
    return False

def element_exists(driver, by, element):
    return len(driver.find_elements(by, element)) > 0