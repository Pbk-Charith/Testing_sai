import requests
import m
import pytest

def test_get_coin():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    return response.json()

def test_get_coin(request_mock):
    
