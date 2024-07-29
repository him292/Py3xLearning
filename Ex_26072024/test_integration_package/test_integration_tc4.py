# Integration Scenario

# 4. Create a booking and delete it
import requests
import pytest
import allure


@pytest.fixture()
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


@pytest.fixture() # with the help of fixture, we can use directly the return value of a function in another function as an argument
@allure.title("Create a new booking")
def create_booking():
    print("Create Booking ID")

    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}

    payload = {
        "firstname": "Steve",
        "lastname": "Smith",
        "totalprice": 1145,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2020-01-01",
            "checkout": "2021-01-01"
        },
        "additionalneeds": "Lunch"
    }

    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]
    data = response.json()
    booking_id = data["bookingid"]
    print(f"Created Booking ID: {booking_id}")
    return booking_id


@allure.title("#TC4 - Trying to update on a DELETED ID - 404")
@pytest.mark.integration
def test_delete_and_verify_booking(create_booking, create_token):
    URL = "https://restful-booker.herokuapp.com/booking/"

    booking_id = create_booking

    # Delete the booking
    DELETE_URL = URL + str(booking_id)
    cookie_value = "token=" + create_token
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }

    delete_response = requests.delete(url=DELETE_URL, headers=headers)
    assert delete_response.status_code == 201
    print(f"Response Text: {delete_response.text}")
    print(f"Deleted Booking ID: {booking_id}")
