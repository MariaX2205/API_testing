import requests
from http import HTTPStatus
from api.questions_api import api
from utils.assertions import Assert


def test_2_status():
    response = api.list_users()
    assert response.status_code == HTTPStatus.OK


# Assert.validate_schema(res.json()) # эта строчка проверяет что файл кот мы олучим, валидный, не битый

def test_single_user_not_found():
    resp = api.single_user_not_found()
    assert resp.status_code == HTTPStatus.NOT_FOUND


def test_single_user():
    resp = api.single_user()
    res_body = resp.json()
    assert resp.status_code == HTTPStatus.OK
    # Assert.validate_schema(res_body)

    assert res_body["data"]["first_name"] == "Janet"
    example = {
        "data": {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }
    }

    assert example == res_body


def test_create():

    res = api.create("Boris", "Coach")

    assert res.status_code == HTTPStatus.CREATED

    assert res.json()["name"] == "Boris"
    assert res.json()["job"] == "Coach"

    assert api.delete_user(res.json()['id']).status_code == HTTPStatus.NO_CONTENT

