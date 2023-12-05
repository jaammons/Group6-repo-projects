from selenium import webdriver
from django.core.management import call_command
import django
import os

def before_all(context):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")

    django.setup()

    call_command("flush", interactive=False)
    call_command("loaddata", "default.json")

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()

def after_scenario(context, scenario):
    context.driver.quit()
