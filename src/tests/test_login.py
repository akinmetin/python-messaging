import json
from tests.initCase import initCase


class TestUserLogin(initCase):

    def test_successful_login(self):
        # Given
        username = "akin"
        password = "123456789"
        payload = json.dumps({
            "username": username,
            "password": password
        })
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)

        # When
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(str, type(response.json['token']))
        self.assertEqual(200, response.status_code)

    def test_login_with_invalid_email(self):
        # Given
        username = "akin"
        password = "123456789"
        payload = {
            "username": username,
            "password": password
        }
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=json.dumps(payload))

        # When
        payload['username'] = "akin11"
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=json.dumps(payload))

        # Then
        self.assertEqual("Invalid username or password", response.json['message'])
        self.assertEqual(401, response.status_code)

    def test_login_with_invalid_password(self):
        # Given
        username = "akin"
        password = "123456789"
        payload = {
            "username": username,
            "password": password
        }
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=json.dumps(payload))

        # When
        payload['password'] = "12345678"
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=json.dumps(payload))

        # Then
        self.assertEqual("Invalid username or password", response.json['message'])
        self.assertEqual(401, response.status_code)
