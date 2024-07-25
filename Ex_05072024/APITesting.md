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






