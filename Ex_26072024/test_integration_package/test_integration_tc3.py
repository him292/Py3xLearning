# Integration Scenario

# 3. Fetch existing booking ID from GET all booking IDs, UPDATE the booking and verify the modification

import pytest
import allure
import requests


@allure.title("TC-03 GET ALL BOOKING, GET SINGLE ID, UPDATEIT , VERIFY USING GET")
@allure.description(
    "GET an existing booking from GET all bookingid's , Update a booking with that id, Verify with GET request that it is updated")
@pytest.mark.integration
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=payload)
    response_data = response.json()
    token = response_data["token"]
    return token


@allure.title("TC-03 GET ALL BOOKING, GET SINGLE ID, UPDATEIT , VERIFY USING GET")
@allure.description(
    "GET an existing booking from GET all bookingid's , Update a booking with that id, Verify with GET request that it is updated")
@pytest.mark.integration
def test_get_all_booking_id():
    url = "https://restful-booker.herokuapp.com/booking/"
    response = requests.get(url=url)
    response_data = response.json()
    assert response.status_code == 200
    print("Booking IDs are: ", response_data)


@allure.title("TC-03 GET ALL BOOKING, GET SINGLE ID, UPDATEIT , VERIFY USING GET")
@allure.description(
    "GET an existing booking from GET all bookingid's , Update a booking with that id, Verify with GET request that it is updated")
@pytest.mark.integration
def test_get_single_booking_id():
    url = "https://restful-booker.herokuapp.com/booking/19/"
    response = requests.get(url=url)
    response_data = response.json()
    assert response.status_code == 200
    assert response_data["bookingid"] == 19


@allure.title("TC-03 GET ALL BOOKING, GET SINGLE ID, UPDATEIT , VERIFY USING GET")
@allure.description(
    "GET an existing booking from GET all bookingid's , Update a booking with that id, Verify with GET request that it is updated")
@pytest.mark.integration
def test_put_single_booking():
    cookies = "token=" + create_token()
    url = "https://restful-booker.herokuapp.com/booking/19/"
    payload = {
        "firstname": "Michael",
        "lastname": "Joe",
        "totalprice": 134,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2020-01-01",
            "checkout": "2020-01-01"
        },
        "additionalneeds": "Extra pillows please"
}
    headers = {"Content-Type": "application/json", "Cookie": cookies}
    response = requests.put(url=url, headers=headers, json=payload)
    print(f"Response Text: {response.text}")
    data = response.json()
    assert data["firstname"] == "Michael", f"Expected firstname 'Michael' but got {data.get('firstname')}"


@allure.description(
    "GET an existing booking from GET all bookingid's , Update a booking with that id, Verify with GET request that it is updated")
@pytest.mark.integration
def test_get_single_booking_id():
    url = "https://restful-booker.herokuapp.com/booking/19/"
    response = requests.get(url=url)
    data = response.json()
    assert data["firstname"] == "Michael", f"Expected firstname 'Michael' but got {data.get('firstname')}"
    print(data)
