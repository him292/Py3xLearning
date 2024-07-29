import pytest
import requests
import allure


@allure.title("Test get single request by id")
@allure.description("Test get single request by id")
@allure.tag("regression", "p0", "smoke")
@allure.label("owner", "Himanshu Sharma")
@allure.testcase("TC-001", "Test case for get single request by id")
@pytest.mark.smoke
# below function is a get function which will fetch IDs from the restful-booker website
def test_get_single_request_by_id():
    # Now to create a booking (POST), we'd need below:
    # - URL
    # - HTTP Method (POST)
    # - Headers
    # - Authorization
    # - Payload (data) - in JSON, Dict format

    baseurl = "https://restful-booker.herokuapp.com"
    basepath = "/booking"
    url = baseurl + basepath

    headers = {"content-type": "application/json"}
    payload = {
        "firstname": "Rahul",
        "lastname": "Sharma",
        "totalprice": 150,
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

    assert responseData["bookingid"] is not None, "Booking ID is not null"
    firstname = responseData["booking"]["firstname"]
    assert firstname == "Rahul"
    assert responseData["bookingid"] > 0
    assert type(responseData["bookingid"]) == int


@allure.title("Test get single request by id")
@allure.description("Test get single request by id")
@allure.tag("regression", "p0", "smoke")
@allure.label("owner", "Himanshu Sharma")
@allure.testcase("TC-002", "Testing a negative case - Empty payload")
@pytest.mark.smoke
# below function is a get function which will fetch IDs from the restful-booker website
def test_get_single_request_by_id_Negative():
    # this methods checks a negative case for EMPTY PAYLOAD

    baseurl = "https://restful-booker.herokuapp.com"
    basepath = "/booking"
    url = baseurl + basepath

    headers = {"content-type": "application/json"}
    payload = {}

    response = requests.post(url=url, json=payload, headers=headers)
    print(type(url))
    print(type(headers))
    print(type(payload))

    assert response.status_code == 500, "Status code is 500"
