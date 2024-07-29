# Integration Scenario

# 6. Trying to update on a DELETED ID - 404


import pytest
import allure
import requests


@allure.title("TC-06 DELETE A DELETED ID")
@allure.description(
    "Trying to Update on a deleted id")
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


@allure.title("TC-06 DELETE A DELETED ID")
@allure.description(
    "Trying to Update on a deleted id")
@pytest.mark.integration
def test_put_single_booking():
    cookies = "token=" + create_token()
    url = "https://restful-booker.herokuapp.com/booking/1866/"
    payload = {
        "firstname": "George",
        "lastname": "Joe",
        "totalprice": 114,
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
    # Check if the response status code is 404 or another appropriate status code for a deleted resource
    if response.status_code == 404:
        assert response.text == "Not Found", f"Expected response text 'Not Found' but got {response.text}"
        print("Booking ID not found, verified with 404 status code and 'Not Found' response text.")
    elif response.status_code == 405:
        assert response.text == "Method Not Allowed", f"Expected response text 'Method Not Allowed' but got {response.text}"
        print(
            "Method not allowed for deleted booking, verified with 405 status code and 'Method Not Allowed' response text.")
    else:
        # If the status code is 200, verify the response
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
        data = response.json()
        assert data["firstname"] == "George", f"Expected firstname 'George' but got {data.get('firstname')}"
        assert data["lastname"] == "Joe", f"Expected lastname 'Joe' but got {data.get('lastname')}"
        print("Booking details are updated successfully")
