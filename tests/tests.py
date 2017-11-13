from mathemlib import Mathem
import pytest
import json


def test_failed_login(httpserver):
    test = Mathem()
    json_test = json.dumps({'test': 'test'})
    httpserver.serve_content(json_test)
    test.mathem_url = httpserver.url
    assert test.mathem_url.startswith('http://127.0.0.1')
    with pytest.raises(Exception):
        result = test.login()

def test_successful_login(httpserver):
    test = Mathem()
    json_test = json.dumps({'Success': 1})
    httpserver.serve_content(json_test)
    test.mathem_url = httpserver.url
    assert test.mathem_url.startswith('http://127.0.0.1')
    assert test.login() == 'logged in'


def test_get_info():
    test = Mathem()
    result = test.get_info(order_id=12345)
    assert result.lower() == 'not implemented yet'
