its a "Markdown" file

Similar to HTML file

(used for notes) like ReadMe.txt

# Learn API Testing

- Author - Himanshu

## Web Fundamentals of API Testers
- HTTP
  - HTTP Methods/Headers
  - Cookie
  - Resourse HTTP (MIME Types)
  - HTTP Status COdes
  - User Agent
- Authentication vs Authorization
- URL Basics
  - Endpoints
  - Query Param, Path param
- JASON Basics
- XML Basics
- REST-SOAP
- JS Basics (POSTMAN)

## How to perform API Testting

### Documentation
- Swagger (tool)
- Postman

### Execution
- Postman (Tool)
- SoAP UI
- Swagger tools


## HTTP is a protocol to transfer request to server

### Server is an application which can handle client's request and attched to a databses
### A Resource is something that can be trasnferred over the internet
### like HTML, text files, JASON, XML

## Benefits of API Testing 
### API is application programming interface - allows communication
### between 2 or more different applications
### 2 different apps means:-    
    ### a Client application can be made in PHP, C#, HTML
    ### But API testing can be done using any other language like Java, Python

 - Much cheaper than other UI testing
 - cost of bugs are low bcz of early testing
 - ensure reliability 
 - Business logic tests - less test cases as of UI
 - No UI layer
 - As per Testing pyramid, testing efforts are less

### Common bugs in API
- Incorrect status codes
- Incorrect Response data
- Incorrect parameter handling
- Inconsistent data formats
- Authentication issues, headers
- Functional issues
- Performance Issues
- Security Issues


## HTTP Methods
- GET: Retrieve data from a specified resource
- POST: Submit data to be processed to a specified resource
- PUT: Update a specified resource
- DELETE: Delete a specified resource
- PATCH: Partially modify a specified resource



### HTTP Status Codes
### These are the signals shown by the server to the client

- 1xx(Informational): Request received, continuing process
- 2xx (Success): Request successfully received
- 3xx(Redirection): FUrther action needs to be taken to complete the request
- 4xx (Client Error): Request contains bad syntax
- 5xx (Server Error): Server failed to validate/complete request


## POSTMAN BASICS
  ### Authorization (Key): Helps you access server API
  ### we send the below only in headers only

  - Basic Auth
  - Digest
  - API Key
  - Tokens
  - OAuth 1.0
  - OAuth 2.0
  - Bearer Token/JWT

### JSON - Java script object notation
### It is used to transfer data from client to server
- Its a lightweight data-interchange format
- Key-value pair
- JSON - Objects & Arrays
- Datatypes Supported:
  - String
  - Number
  - Boolean
  - Null
  - Array
  - Object
Ex:

{
  "name": "Himanshu",
  "age":  20,
  "number": "9820417287"
}

Ex: JSON within JSON

{
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": true,
  "members":
    {
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes"
    }
}


### XML (Extensible Markup Language)
### Also used to store and transfer the data

## SOAP Web Service
### Simple object access protocol

- SOAP is based on XML
- More secure
- 

## POSTMAN Basics 
### refer to Postman tool

## To perform reporting  install NEWMAN tool (ie. POSTMAN commandline)
### Newman is only used to run the scripts via commandline (Like we do in Postman via UI)

- Run the code in Newman (Postman Command line and create HTML Report):
- For the above we need to do below:
  - Install NodeJS
    - Go to terminal and type: node --version and then, npm --version to verify installation
  - Install Newman (Command - `npm install -g newman`)
    - verify via: newman --version
  - Run below command to activate the plugin for HTML reports
    - npm i newman-reporter-htmlextra

## MANUAL TESTING (Manual Way)
How to run a collection using Newman (Commandline):
- Create a repository where we'll keep our SOAP requests
  - copy the collection link from Postman (From Share command)
  - paste this command in Newman command line and then reporting type you want
    - Ex: newman run "https://api.postman.com/collections/37172451-68867e89-3f45-4839-aa85-9b9081e5aead?access_key=PMAT-01J3HWDWHPYR4W3KVQ5GY9Z4C8" -r cli,htmlextra
  - Now to open the html report, run the below command:
    - open "/Users/datashan/Desktop/PostmanRepo/SOAPDemo/newman/API Testing - SOAP Project 1-2024-07-24-08-25-37-142-0.html"

## REST API
### Its the representational state transfer

### Import the REST API into POSTMAN | Collection & Testcases
2 Ways:
- with API Docmentation:
  - CURL request - command line request to work with the REST APIs
  - URLs
  - HTTP Methods
  - Authorization, Tokens, Cookie
  - Payload JSON, XML
  - How to verify Response
  - Status code

## Project #2
- Create booking with valid data
- create booking with invalid first name (null)
- Invalid JSON
- invalid total price
- empty values of all fields
- invalid mandatory
- min and mx values for all - Total=11000000000000000222002002
- Invalid URL
- Deposit false
- Long name
- Arabic names
- Different date formats
- Special chars
- Reponse time

Integration Scenario:
- Create a booking-> Update the booking name -> Get booking id and verify
- Create a booking-> delete the booking name -> Get booking id and verify if it exists
- Create a booking-> delete the booking name 
- Get existing booking-> Update the booking name -> Get booking id and verify


- without API Documentation:
  - create a rough high level documentation for yourself
  - which Modules we have to test
  - create a collection based on that
  - We need to figure out below:
    - URL
    - Payload
    - HTTP Methods
    - Status codes
    - What to verify
    - Request body
    - Header, Auth, Cookie, Tokens

### To start working with POSTMAN, you need to do below: ( And to fetch the URLs for API Testing)
- Open the desired website (that you want to work on)
- Go to the login page (keeping the inspect window open)
  - Go to NETWORK tab
- Now, fillin all the details in the creation page and click on create button
- Now, you can have the POST request details within the NETWORK tab, from there,
  - Rightclick on the request and click on the "Copy CURL request"
- Now, paste this CURL URL within the POSTMAN