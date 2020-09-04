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

| Request Type          | Endpoint                    | What it does                                       |
| -----------------     |:--------------------------- |:-------------------------------------------------- |
| ``GET``               | /api/Sales/All              | Returns list of sold article details.              |
| ``GET``               | /api/Sales/All/Revenue      | Returns list of revenues by article numbers.       |
| ``GET``               | /api/Sales/Daily            | Returns count of sold articles by day.             |
| ``GET``               | /api/Sales/Daily/Revenue    | Returns list of article revenues by day.           |
| ``POST``              | /api/Sales/Add/Sale         | Adds new sale into memory/database.                |