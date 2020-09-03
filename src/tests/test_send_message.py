import json
from tests.initCase import initCase

class TestSendPrivateMessage(initCase):

    def test_successful_send_message(self):
        # Given
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