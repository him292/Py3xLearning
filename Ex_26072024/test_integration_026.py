# Fixtures: Concept in Python

#  A fixture is a function that provides a fixed value for one or more tests.
# Fixtures are used to set up the necessary preconditions for testing, such as creating temporary files, databases, or initializing objects.

# For example, we have a similar case of booking then,
# To update a booking, we need to create a booking first, create a token as well. This can be done using a fixture.

# two methods:
# 1. Setup() - for Pre-conditions
# 2. TearDown() - for Post-conditions

# If we want to modularize our code, (Setup and Teardown) methods, we should move them within the conftest.py file, so that
# these methods are available to the whole project'
# - No need to import conftest file within your project to use the methods within it
# - Python automatically realizes the conftest file before running any program

# so always move the fixture methods (who you think will be used everywhere) into the conftest file

import pytest


def test_update_booking(create_token, create_booking):
    # Test logic to update the booking
    assert create_token == "token123", "Token creation success"
    assert create_booking == "booking123", "Booking creation success"
    print("Token is ", create_token)
    print("Booking is ", create_booking)
