# coding: utf-8
from mathemlib import Mathem, LoginError
import pytest
import json
import requests
import logging

# Disable all logging outputs
logger = logging.basicConfig(level=logging.disable(logging.CRITICAL))


def test_failed_credentials_login(httpserver):
    test = Mathem()
    httpserver.serve_content('Felaktigt användarnamn eller lösenord')
    test.mathem_url = httpserver.url
    assert test.mathem_url.startswith('http://127.0.0.1')
    with pytest.raises(LoginError):
        test.login()


def test_failed_login_exception(httpserver):
    test = Mathem()
    httpserver.serve_content('unexpected response')
    test.mathem_url = httpserver.url
    assert test.mathem_url.startswith('http://127.0.0.1')
    with pytest.raises(ValueError):
        test.login()


def test_successful_login(httpserver):
    test = Mathem()
    httpserver.serve_content(json.dumps({'Success': True}), code=200)
    test.mathem_url = httpserver.url
    assert test.mathem_url.startswith('http://127.0.0.1')
    response = test.login()
    assert isinstance(response, dict)
    assert response.get('Success')


def test_get_orders(httpserver):
    test = Mathem()
    with open('test_orders.html') as f:
        test_orders = f.read()
    httpserver.serve_content(test_orders)
    test.mathem_url = httpserver.url
    test.session = requests.session()
    result = test.get_orders(limit=3)
    assert isinstance(result, dict)
    assert len(result) == 3
    assert result.get('20316076') == {}


def test_get_info():
    test = Mathem()
    result = test.get_info(order_id=12345)
    assert result.lower() == 'not implemented yet'
