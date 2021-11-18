import pytest
import requests
import json
from .factories import RequestFactory

base_url = 'http://localhost:5000/request'
headers = {'Content-Type': 'application/json'}


def test_factory(book_request):
    response = requests.get(base_url, headers=headers)

    assert response.status_code == 200
    assert book_request.title in response.text


# Add new request
def test_add_request():
    data = {
        "title": "Foundation",
        "email": "email@gmail.com"
    }
    response = requests.post(base_url, json.dumps(data), headers=headers)

    assert response.status_code == 201
    assert data['title'] in response.text


def test_add_request_fail_bad_title():
    data = {
        "title": "Foundation - title doesn't exist",
        "email": "email@gmail.com"
    }
    response = requests.post(base_url, json.dumps(data), headers=headers)
    assert response.status_code == 400


def test_add_request_fail_bad_email():
    data = {
        "title": "Foundation",
        "email": "@email@gmail.com"
    }
    response = requests.post(base_url, json.dumps(data), headers=headers)
    assert response.status_code == 400


# Get Request by ID
def test_get_request(book_request):
    url = f"{base_url}/{book_request.id}"
    response = requests.get(url)

    assert response.status_code == 200


def test_get_request_fail():
    url = base_url + '/100'
    response = requests.get(url)
    assert response.status_code == 404


# Get all requests
def test_get_all_requests():
    response = requests.get(base_url)
    assert response.status_code == 200


# Delete request by id
def test_delete_request(book_request):
    url = f"{base_url}/{book_request.id}"
    response = requests.delete(url)

    assert response.status_code == 200
