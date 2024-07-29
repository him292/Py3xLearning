# Integration Scenario

# 5. Invalid creation - enter a wrong payload or wrong JSON
import requests
import pytest
import allure


@allure.title("TC-05 CREATE A BOOKING WITH INVALID JSON")
@allure.description("Enter a wrong payload or JSON")
@pytest.mark.integration
def test_create_booking():
    booking_url = "https://restful-booker.herokuapp.com/booking/"
    headers = {"Content-Type": "application/json"}
    payload = {}
    response = requests.post(url=booking_url, headers=headers, json=payload)
    assert response.status_code == 500
    print(response)
