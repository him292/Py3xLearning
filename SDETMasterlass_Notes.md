# SELENOID

- Basically, its a powerful tool for running selenium tests in Docker container
- EX: If you have 1000s of test cases to run in a limited period of time, the you can assign these test cases to
- Selenoid and it will further assign to multiple machines (which is call Selenium grid) for execution.
- Here, SELENOID will act as a HUB and Machines will acts as a NODE


### POSTMAN Testcases writing

Lets say we have below JSON response as an example:

{
    "firstname" : "Rahul",
    "lastname" : "Sharma",
    "totalprice" : 150,
    "depositpaid" : true,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Lunch"
}

Now, we need have below test cases according to above JSON

1. bookingid = 505
2. firstname == Amit
3. firstname should be string
4. should get 200 as response
5. content type of headers = Application/Json
6. Total price > 0

Now, we can write testcases in POSTMAN (Check- Create Booking_TesCaseWriting file in Postman)


## POSTMAN Variables
- These are basically used, when we know a certain variables that are common to our tests and will be used repetitively then
we add these variables within the variables section. These variables helps in cases like where there are a lot of test cases
to be tested and we have multiple environments to test. Now, there are 5 types of variables:

1. Global Variable: This variable is available to all the collections within Postman
2. Collection variable: Only works within a specific collection
3. Environment variables: can create environemnts like QA, PROD (variables bound within these environments) - this passes information/data from one request to the other (like token, bookingid)
4. Data Variables (used in DDT) - its about testing the data present within the CSV file (like login tests). It is driven by the CSV file, so once we run a collection, we need to import
   the CSV file before running the tests. It will run all the cases automatically (Pre-req: need to prepare the CSV data)
5. Local Variables: Variables created in functions (written in scripts section)

### API Testing with POSTMAN Advance
Here, will understand how we can work with postman variables ( Headers)

Collection variables

Ex: in the restful booker example
- to update a booking, we're creating a booking a getting the ID from there
- then, we're creaing a token (for Auth) to be used within the PUT request
- then, we're able to update the booking (using token and bookingID as VARIABLES)
  - Just like within python, we use decorators/fixtures to use the "token & bookingiD" within the update function 