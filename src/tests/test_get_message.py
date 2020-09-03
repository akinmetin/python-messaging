import json
from tests.initCase import initCase

class TestGetPrivateMessage(initCase):

    def test_successful_private_messaging(self):
        # Signup and login with "akin"
        username = "akin"
        password = "123456789"
        user_payload = json.dumps({
            "username": username,
            "password": password
        })

        self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=user_payload)
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=user_payload)
        login_token = response.json['token']

        message_payload = {
            "receiver": "metin",
            "message": "test message",
            "sent_by": username
        }
        # When
        response = self.app.put('/api/message/metin',
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
            data=json.dumps(message_payload))

        # Then
        self.assertEqual(200, response.status_code)
        
        # Signup and login with "metin"
        username = "metin"
        password = "123456789"
        user_payload = json.dumps({
            "username": username,
            "password": password
        })

        self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=user_payload)
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=user_payload)
        login_token = response.json['token']
        
        response = self.app.get('/api/message/akin',
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"})
        
        self.assertEqual("test message", response.json[0]['message'])
        self.assertEqual(200, response.status_code)