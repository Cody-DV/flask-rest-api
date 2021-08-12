import pytest
import requests
import json
from .factories import BookFactory

base_url = 'http://localhost:5000/request'
headers = {'Content-Type': 'application/json'}


def test_factory():
    # books = BookFactory.create_batch(size=4)
    #
    book = BookFactory.create(title="Test Book")
    # for book in books:
    #     print(f'Title: {book.title}')

    response = requests.get(base_url, headers=headers)

    print(response.json)
    breakpoint()

    assert book.title in response.json


# Add new request
def test_add_request():
    data = {
        "title": "Foundation",
        "email": "email@gmail.com"
    }
    response = requests.post(base_url, json.dumps(data), headers=headers)
    assert response.status_code == 201


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
def test_get_request():
    url = base_url + '/1'
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
def test_delete_request():
    response = requests.delete(base_url + '/1')
    assert response.status_code == 200
