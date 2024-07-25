import pytest
import allure


@allure.title("TC1: Test Subtraction of 2-1==1")
@allure.description("This test verifies the subtraction of 2-1=1")
@pytest.mark.regression
def test_subtraction1():
    assert 2 - 1 == 1

@allure.title("TC2: Test Addition of 1+1==2")
@allure.description("This test verifies the addition of 1+1=2")
@pytest.mark.sanity
def test_addition1():
    assert 1 + 1 == 2

@allure.title("TC3: Test Addition of 12+1==13")
@allure.description("This test verifies the addition of 12+1=13")
@pytest.mark.smoke
def test_addition2():
    assert 12 + 1 == 13

@allure.title("TC4: Test Addition of 4+4==8")
@allure.description("This test verifies the addition of 4+4==8")
@pytest.mark.regression
def test_addition3():
    assert 4 + 4 == 8

@allure.title("TC5: Test Addition of 0+0!=0")
@allure.description("This test verifies the addition of 0+0!=0")
@pytest.mark.skip(reason="This test is not complete")
def test_addition4():
    assert 0 + 0 != 0
