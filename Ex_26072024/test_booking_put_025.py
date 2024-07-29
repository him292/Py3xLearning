# What we need for a PUT request
import requests
import pytest
import allure


# URL - booking ID exist
# PathParam
# Token - for authorization
# Payload - updated

def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content_Type": "application/json"}
    payload = {
        "username": "admin",
        "password": "password123"
    }

    response = requests.post(url=url, json=payload, headers=headers)
    token = response.json()["token"]
    print('Token is: ', token)
    return token


def create_booking():
    baseurl = "https://restful-booker.herokuapp.com"
    basepath = "/booking"
    url = baseurl + basepath

    headers = {"content-type": "application/json"}
    payload = {
        "firstname": "Keshav",
        "lastname": "Sharma",
        "totalprice": 151,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Lunch"
    }

    response = requests.post(url=url, json=payload, headers=headers)

    assert response.status_code == 200, "Status code is 200"

    # here we are storing the response in JSON to be used further
    responseData = response.json()
    # Now we're adding the validations below:

    booking_id = responseData["bookingid"]
    return booking_id


def test_put_request_positive():
    baseurl = "https://restful-booker.herokuapp.com"
    basepath = "/booking/" + str(create_booking())
    PUT_url = baseurl + basepath

    cookie = "token=" + create_token()

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }

    json_payload = {
        "firstname": "Raghu",
        "lastname": "Sharma",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=PUT_url, json=json_payload, headers=headers)
    assert response.status_code == 200, "Status code is 200"
    data = response.json()
    assert data["firstname"] == "Raghu", "First name is updated"


def test_request_delete():
    baseurl = "https://restful-booker.herokuapp.com"
    bookingid = create_booking()
    DEL_url = baseurl + str(bookingid)

    cookie = "token=" + create_token()

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }

    response = requests.delete(url=DEL_url, headers=headers)
    assert response.status_code == 201, "Status code is 201"
    data = response.json()
    assert data["created"] == True, "Booking is deleted"
