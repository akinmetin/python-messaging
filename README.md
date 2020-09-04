# Python Messaging API

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/ccf76489b9074368bf86218383dfcbbe)](https://www.codacy.com/manual/metin_akin_bursa/python-messaging?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=akinmetin/python-messaging&amp;utm_campaign=Badge_Grade)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

![Python Badge](https://img.shields.io/badge/python-3.7%20|%203.8-blue)
![Docker](https://img.shields.io/badge/Docker-blue)

### Installing

* Download this repository and extract it to any folder.
* Build and run it using Docker, then you will be able to send requests via Postman.

### Allowed HTTPs requests:
| Request Type | Use                                 |
| ------------ |:----------------------------------- |
| PUT          | To create resource                  |
| POST         | Update resource                     |
| GET          | Get a resource or list of resources |
| ~~DELETE~~   | ~~To delete resource~~              |

### Description Of Usual Server Responses:

* 200 OK - the request was successful.
* 201 Created - the request was successful and a resource was created.
* 204 No Content - the request was successful but there is no representation to return (i.e. the response is empty).
* 400 Bad Request - the request could not be understood or was missing required parameters.
* 401 Unauthorized - authentication failed or user doesn't have permissions for requested operation.
* 403 Forbidden - access denied.
* 404 Not Found - resource was not found.
* 405 Method Not Allowed - requested method is not supported for resource.
* 500 Internal Server Error - the server encountered an unexpected condition which prevented it from fulfilling the request.

## Endpoints

| Request Type          | Endpoint                    | What it does                                               |
| -----------------     |:--------------------------- |:---------------------------------------------------------- |
| ``GET``, ``PUT``      | /api/message/<target>       | Send and get private message with another user             |
| ``GET``               | /api/message/archive        | Returns all sent and received messages of authorized user  |
| ``PUT``               | /api/block/<target>         | Block another user to communicate with authorized user     |
| ``POST``              | /api/auth/signup            | User sign up endpoint                                      |
| ``POST``              | /api/auth/login             | User login endpoint                                        |

## Example API Calls

Endpoint: ``POST /api/auth/signup``

Input:
```
{
    "username": "metin",
    "password": "123456789"
}
```
Output:
```
{
    "message": "Signup Success"
}
```

Endpoint: ``POST /api/auth/login``

Input:
```
{
    "username": "metin",
    "password": "123456789"
}
```
Output:
```
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1OTkyMTc4NDIsIm0MiwianRpIjoiOGQ2Zjg4MzAt..."
}
```

Endpoint: ``PUT /api/message/akin``

Input: (extra Bearer token field is required)
```
{
    "message": "hello"
}
```
Output:
```
{
    "message": "Message is successfully sent"
}
```

Endpoint: ``GET /api/message/metin``

Input: (using ``akin`` user, extra Bearer token field is required)

Output:
```
[
    {
        "_id": {
            "$oid": "5f52222ed36baf102fb2e999"
        },
        "receiver": "akin",
        "message": "hello",
        "sent_by": "metin",
        "created_at": {
            "$date": 1599217338958
        },
        "read": 0
    },
    {
        "_id": {
            "$oid": "5f522305d36baf102fb2e99d"
        },
        "receiver": "metin",
        "message": "hey",
        "sent_by": "akin",
        "created_at": {
            "$date": 1599217338958
        },
        "read": 0
    }
]
```

Endpoint: ``GET /api/message/archive``

Input: (using ``akin`` user, extra Bearer token field is required)

Output:
```
[
    {
        "_id": {
            "$oid": "5f52222ed36baf102fb2e999"
        },
        "receiver": "akin",
        "message": "hello",
        "sent_by": "metin",
        "created_at": {
            "$date": 1599217338958
        },
        "read": 0
    },
    {
        "_id": {
            "$oid": "5f522305d36baf102fb2e99d"
        },
        "receiver": "metin",
        "message": "hey",
        "sent_by": "akin",
        "created_at": {
            "$date": 1599217338958
        },
        "read": 0
    },
    {
        "_id": {
            "$oid": "5f522374d36baf102fb2e9a0"
        },
        "receiver": "ali",
        "message": "im just coding",
        "sent_by": "akin",
        "created_at": {
            "$date": 1599217338958
        },
        "read": 0
    }
]
```

Endpoint: ``PUT /api/block/metin``

Input: (extra Bearer token field is required)
Output:
```
{
    "message": "User is successfully blocked"
}
```

## Testing

Test cases can be found in ``src/tests`` folder.

All test cases are passing.

Coverage test results are:
![Image of Yaktocat](https://github.com/akinmetin/python-messaging/blob/master/img/coverage-report.jpg?raw=true)