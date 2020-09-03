import json
from tests.initCase import initCase

class TestArchive(initCase):

    def test_successful_get_archive(self):
        # Signup and login with "akin" / 1st message to "metin"
        username = "akin"
        password = "123456789"
        user_payload = json.dumps({
            "username": username,
            "password": password
        })

        # post the data into signup and login  endpoints
        self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=user_payload)
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=user_payload)
        login_token = response.json['token']

        message_payload = {
            "receiver": "metin",
            "message": "test message 1",
            "sent_by": username
        }
        # send a message to "metin" using message endpoint
        response = self.app.put('/api/message/metin',
                                headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                data=json.dumps(message_payload))

        # check the equality of response data's status code and expected status code
        self.assertEqual(200, response.status_code)

        # Signup and login with "mete" / 2nd message to "metin"
        username = "mete"
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
            "receiver": "metin",
            "message": "test message 2",
            "sent_by": username
        }
        # send a message to "metin" using message endpoint
        response = self.app.put('/api/message/metin',
                                headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                data=json.dumps(message_payload))

        # check the equality of response data's status code and expected status code
        self.assertEqual(200, response.status_code)

        # Signup and login with "metin" to check archive
        username = "metin"
        password = "123456789"
        user_payload = json.dumps({
            "username": username,
            "password": password
        })

        # post the data into endpoints
        self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=user_payload)
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=user_payload)
        login_token = response.json['token']

        # get messages from "akin" using message endpoint
        response = self.app.get('/api/message/archive',
                                headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"})

        # check the equality of response data and expected data
        self.assertEqual("test message 1", response.json[0]['message'])
        self.assertEqual("test message 2", response.json[1]['message'])
        self.assertEqual(200, response.status_code)
