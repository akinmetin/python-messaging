import json
from tests.initCase import initCase

class TestPrivateMessage(initCase):

    def test_successful_send_private_message(self):
        # Signup and login with "akin"
        username = "akin"
        password = "123456789"
        user_payload = json.dumps({
            "username": username,
            "password": password
        })

        # post the data into signup and login endpoints
        self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=user_payload)
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=user_payload)
        login_token = response.json['token']

        message_payload = {
            # "receiver": "metin",
            "message": "test message",
            "sent_by": username
        }
        # send a message to "metin" using message endpoint
        response = self.app.put('/api/message/metin',
                                headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                data=json.dumps(message_payload))

        # check the equality of response data's status code and expected status code
        self.assertEqual("Message is successfully sent", response.json[0]['message'])
        self.assertEqual(200, response.status_code)

    def test_successful_get_private_message(self):
        # Signup and login with "akin"
        username = "akin"
        password = "123456789"
        user_payload = json.dumps({
            "username": username,
            "password": password
        })

        # post the data into signup and login endpoints
        self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=user_payload)
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=user_payload)
        login_token = response.json['token']

        message_payload = {
            # "receiver": "metin",
            "message": "test message",
            "sent_by": username
        }
        # send a message to "metin" using message endpoint
        response = self.app.put('/api/message/metin',
                                headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                data=json.dumps(message_payload))

        # check the equality of response data's status code and expected status code
        self.assertEqual(200, response.status_code)

        # Signup and login with "metin"
        username = "metin"
        password = "123456789"
        user_payload = json.dumps({
            "username": username,
            "password": password
        })

        # post the data into signup and login endpoints
        self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=user_payload)
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=user_payload)
        login_token = response.json['token']

        # get messages from "akin" using message endpoint
        response = self.app.get('/api/message/akin',
                                headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"})

        # check the equality of response data and expected data
        self.assertEqual("test message", response.json[0]['message'])
        self.assertEqual(200, response.status_code)

    def test_send_message_to_blocked_user(self):
        # Signup and login with "akin"
        username = "akin"
        password = "123456789"
        user_payload = json.dumps({
            "username": username,
            "password": password
        })

        # post the data into signup and login endpoints
        self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=user_payload)
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=user_payload)
        login_token = response.json['token']

        # send a message to "metin" using message endpoint
        response = self.app.put('/api/block/metin',
                                headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"})

        # check the equality of response data's status code and expected status code
        self.assertEqual("User is successfully blocked", response.json[0]['message'])
        self.assertEqual(200, response.status_code)

        # Signup and login with "metin"
        username = "metin"
        password = "123456789"
        user_payload = json.dumps({
            "username": username,
            "password": password
        })

        # post the data into signup and login endpoints
        self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=user_payload)
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=user_payload)
        login_token = response.json['token']

        message_payload = {
            # "receiver": "metin",
            "message": "test message",
            "sent_by": username
        }
        # send a message to "metin" using message endpoint
        response = self.app.put('/api/message/akin',
                                headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                data=json.dumps(message_payload))

        # check the equality of response data and expected data
        self.assertEqual("Communication between you and the target is blocked", response.json['message'])
        self.assertEqual(403, response.status_code)
