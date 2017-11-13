from mathemlib import Mathem
import pytest
import json
import requests


def test_failed_login(httpserver):
    test = Mathem()
    json_test = json.dumps({'test': 'test'})
    httpserver.serve_content(json_test)
    test.mathem_url = httpserver.url
    assert test.mathem_url.startswith('http://127.0.0.1')
    with pytest.raises(Exception):
        test.login()


def test_successful_login(httpserver):
    test = Mathem()
    json_test = json.dumps({'Success': 1})
    httpserver.serve_content(json_test)
    test.mathem_url = httpserver.url
    assert test.mathem_url.startswith('http://127.0.0.1')
    assert test.login() == 'logged in'


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
