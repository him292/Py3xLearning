# REQUEST Module
# Module is a package or library that contains functions which you can use easily
# like math, os, csv, allure, pytest

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
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print(responseData.json())
    assert responseData.status_code == 200, "Status code is not 200"


@allure.title("Test get single request by id - negative case")
@allure.description("Test get single request by id with invalid booking ID")
@pytest.mark.smoke
def test_get_single_request_by_negative():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    responseData = requests.get(url)
    # print(responseData.json()) # removed because there is no json response for invalid data
    print(responseData.text)
    assert responseData.status_code == 404, "Status code is not 404"
