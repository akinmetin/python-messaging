class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class AlreadyExistsError(Exception):
    pass

class NotExistsError(Exception):
    pass

class UsernameAlreadyExistsError(Exception):
    pass

class UnauthorizedError(Exception):
    pass

errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400
    },
    "AlreadyExistsError": {
        "message": "User with the given username already exists",
        "status": 400
    },
    "NotExistsError": {
        "message": "Message doesn't exists",
        "status": 400
    },
    "UsernameAlreadyExistsError": {
        "message": "User with given username address already exists",
        "status": 400
    },
    "UnauthorizedError": {
        "message": "Invalid username or password",
        "status": 401
    }
}
