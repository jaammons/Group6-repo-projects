import requests
import pytest
import json

REGISTRATION_FORM_FIELDS = {"username": "RegistrationTest", "email": "Testuser@gmail.com", "password": "Register123", "confirmation": "Register123"}

def test_welcome(live_server):
    response = requests.get(live_server.url + "/welcome")
    assert response.status_code == 200
    assert response.text == 'Welcome to Our Ecommerce Site!'


def test_registration(live_server):
    
    response = requests.post(live_server.url + "/users/register_user", data=REGISTRATION_FORM_FIELDS)
    assert response.status_code == 200
    
    # Get the data from the response
    data = json.loads(response.json())

    assert data["Success"] == "New user created."

def test_cookies(live_server):
    
    response = requests.get(live_server.url + "/users/get_cookie")
    cookie_monster_says = response.cookies["cookie"][1:-1]
    assert cookie_monster_says == "COOKIE! Om nom nom nom."


