import json
from tests.initCase import initCase


class TestUserLogin(initCase):

    def test_successful_login(self):
        # initial json data
        username = "akin"
        password = "123456789"
        payload = json.dumps({
            "username": username,
            "password": password
        })
        # post the data into signup endpoint
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)

        # post the data into login endpoint
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=payload)

        # check the equality of response data and expected data
        self.assertEqual(str, type(response.json['token']))
        self.assertEqual(200, response.status_code)

    def test_login_with_invalid_email(self):
        # initial json data
        username = "akin"
        password = "123456789"
        payload = {
            "username": username,
            "password": password
        }
        # post the data into signup endpoint
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=json.dumps(payload))

        # post the data into login endpoint
        payload['username'] = "akin11"
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=json.dumps(payload))

        # check the equality of response data and expected data
        self.assertEqual("Invalid username or password", response.json['message'])
        self.assertEqual(401, response.status_code)

    def test_login_with_invalid_password(self):
        # initial json data
        username = "akin"
        password = "123456789"
        payload = {
            "username": username,
            "password": password
        }
        # post the data into signup endpoint
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=json.dumps(payload))

        # post the data into login endpoint
        payload['password'] = "12345678"
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=json.dumps(payload))

        # check the equality of response data and expected data
        self.assertEqual("Invalid username or password", response.json['message'])
        self.assertEqual(401, response.status_code)
