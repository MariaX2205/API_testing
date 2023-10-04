from api.httpbin_api import http_bin_api
from http import HTTPStatus
import requests
import re


def test_list_html():
    res = http_bin_api.list_html()
    assert res.status_code == HTTPStatus.OK
    assert res.headers['Content-Type'] == 'text/html; charset=utf-8'


def test_robots():
    res = http_bin_api.robots_txt()
    assert res.status_code == HTTPStatus.OK
    assert res.headers['Content-Type'] == 'text/plain'
    assert re.fullmatch(r'.*User-agent: \*.*Disallow: /deny.*', res.text, flags=re.DOTALL)


def test_bin_org():
    res = http_bin_api.bin_org()
    res_body = res.json()
    assert res.status_code == HTTPStatus.OK
    if res.headers['Content-Type'] == 'application/json':
        #Assert.validate_schema(res.json())

        origin = res.json()['origin']
        assert re.fullmatch(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', origin)