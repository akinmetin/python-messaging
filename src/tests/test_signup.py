import json
from tests.initCase import initCase


class SignupTest(initCase):

    def test_successful_signup(self):
        # Given
        payload = json.dumps({
            "username": "metin",
            "password": "123456789"
        })

        # When
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(200, response.status_code)

    def test_signup_with_extra_field(self):
        #Given
        payload = json.dumps({
            "username": "metin",
            "name": "metin",
            "password": "123456789"
        })

        #When
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual('Request is missing required fields', response.json['message'])
        self.assertEqual(400, response.status_code)

    def test_signup_without_username(self):
        #Given
        payload = json.dumps({
            "password": "123456789",
        })

        #When
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual('Something went wrong', response.json['message'])
        self.assertEqual(500, response.status_code)

    def test_signup_without_password(self):
        #Given
        payload = json.dumps({
            "username": "metin",
        })

        #When
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual('Something went wrong', response.json['message'])
        self.assertEqual(500, response.status_code)

    def test_creating_already_existing_user(self):
        #Given
        payload = json.dumps({
            "username": "metin",
            "password": "123456789"
        })
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)

        # When
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual('User with the given username already exists', response.json['message'])
        self.assertEqual(400, response.status_code)
