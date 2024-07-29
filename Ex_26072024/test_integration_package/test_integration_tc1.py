# Integration Scenario

# 1. verify that create booking -> Patch request -> verify that firstname is updated

# What we need for a PUT request
import requests
import pytest
import allure


def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
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
        "firstname": "Himanshu",
        "lastname": "Sharma",
        "totalprice": 159,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2021-01-01",
            "checkout": "2021-01-01"
        },
        "additionalneeds": "Lunch"
    }

    response = requests.post(url=url, json=payload, headers=headers)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    responseData = response.json()
    booking_id = responseData["bookingid"]
    print('Booking ID is: ', booking_id)
    return booking_id


def test_put_request_positive():
    baseurl = "https://restful-booker.herokuapp.com"
    booking_id = create_booking()
    basepath = "/booking/" + str(booking_id)
    PUT_url = baseurl + basepath

    cookie = "token=" + create_token()

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }

    json_payload = {
        "firstname": "Deepanshu",
        "lastname": "Sharma",
        "totalprice": 140,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    print(f"PUT URL: {PUT_url}")
    print(f"Headers: {headers}")
    print(f"Payload: {json_payload}")

    response = requests.put(url=PUT_url, json=json_payload, headers=headers)
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    data = response.json()
    assert data["firstname"] == "Deepanshu", f"Expected firstname 'Deepanshu' but got {data.get('firstname')}"
    print("First name is updated successfully")
