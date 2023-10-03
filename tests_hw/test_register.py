import requests
from http import HTTPStatus
from api.questions_api import api
from utils.assertions import Assert


def test_register():
    res = api.register_user("eve.holt@reqres.in", "112233")
    res_body = res.json()
    assert res.status_code == HTTPStatus.OK

    # Assert.validate_schema(res_body)

    assert res_body["id"] == 4
    assert res_body["token"] == "QpwL5tke4Pnpja7X4"
    example = {
        "id": 4,
        "token": "QpwL5tke4Pnpja7X4"
    }
    assert example == res_body


def test_reg_unsuccessful():
    res = api.register_user("eve.holt@reqres.in", "")
    res_body = res.json()
    assert res.status_code == HTTPStatus.BAD_REQUEST
    assert res_body["error"] == "Missing password"
    example = {
        "error": "Missing password"
    }
    assert example == res_body
