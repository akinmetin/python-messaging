import json
from tests.initCase import initCase


class SignupTest(initCase):

    def test_successful_signup(self):
        # initial json data
        payload = json.dumps({
            "username": "metin",
            "password": "123456789"
        })

        # post the data into signup endpoint
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)

        # check the equality of response status code and expected data
        self.assertEqual(200, response.status_code)

    def test_signup_with_extra_field(self):
        # initial json data
        payload = json.dumps({
            "username": "metin",
            "name": "metin",
            "password": "123456789"
        })

        # post the data into signup endpoint
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)

        # check the equality of response data and expected data
        self.assertEqual('Request is missing required fields', response.json['message'])
        self.assertEqual(400, response.status_code)

    def test_signup_without_username(self):
        # initial json data
        payload = json.dumps({
            "password": "123456789",
        })

        # post the data into signup endpoint
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)

        # check the equality of response data and expected data
        self.assertEqual('Something went wrong', response.json['message'])
        self.assertEqual(500, response.status_code)

    def test_signup_without_password(self):
        # initial json data
        payload = json.dumps({
            "username": "metin",
        })

        # post the data into signup endpoint
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)

        # check the equality of response data and expected data
        self.assertEqual('Something went wrong', response.json['message'])
        self.assertEqual(500, response.status_code)

    def test_creating_already_existing_user(self):
        # initial json data
        payload = json.dumps({
            "username": "metin",
            "password": "123456789"
        })
        # post the data into signup endpoint
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)

        # post the data into signup endpoint
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)

        # check the equality of response data and expected data
        self.assertEqual('User with the given username already exists', response.json['message'])
        self.assertEqual(400, response.status_code)
