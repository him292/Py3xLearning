## Javascript Notes

### we'd need to learn JS basics so that we can write our own custom scripts within POSTMAN

- pm.test is used to get the test results within the console of POSTMAN
- pm.expect to add the conditions to get the expected results for tests

### E2E Test case - Automation Exercise (check POSTMAN Project)

- Create New Booking
- Update booking
- Get the booking details

Now, in the above scenario, we need to automate the test case in a way so that the created
booking id gets aumatically passed on to the update booking and the to "get bookng details"
test case

There are total 3 ways we can pass the "new booking id" to all the test cases:
1. By declaring the variables globally (in env variable section)
  - Now, if for ex: we add "Content-Type to application/json" globally, then we can use this value
  - everywhere we used content-Type, we just now need to add the value "{{content-type}}"
  - within the HEADERS section of the collection
2. IF YOU WANT TO RESTRICT the accessibility, then add the variable within the VARIABLE
  - tab of the collection
    By declaring the variables locally (within a collection)
3. Creating ENVIRONMENT variable like for PROD, QA, Pre-PROD
   - Now, once you provide the variables values within the ENVIRONMENT created,
   - we can replace the value of the variable with the "webservice" url link


## API Automation (using Python)

1. How to make a request
   - using Request Library
   - HTTP Methods (Get, POST etc)
2. How to verify the request
   - Test Framework (Pytest)
3. Logs
4. How to run the code
   - Jenkins + GIT

### Assert Keyword
This means what you want to validate
basically it checks if expected result = actual result

### Annotations ( we use markers/annotations to run a specific test case)
command: pytest -m "smoke" Ex_26072024/test_022.py
- To run a test case with a pattern
  - pytest -k "18" Ex_26072024/test_022.py
- Marking is basically done if there are lot of test cases and then
- you want to run only certain amount 

### How to see the allure report in Pytest
- make sure that allure commandline is installed
- download NodeJS
- node -v
- npm install -g npm allure-commandline
- verify that allure->options
- run your pytestcase - pytest Ex_26072024/test_022.py -alluredir=allure_result
- allure serve allure_result

## Install JDK and then set variable as below
export JAVA_HOME=$(/usr/libexec/java_home)
export PATH=$JAVA_HOME/bin:$PATH
