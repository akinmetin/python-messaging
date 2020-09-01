from flask import Response, request
from flask_jwt_extended import create_access_token
from mongodb.models import User, Logs
from flask_restful import Resource
import datetime


class SignupApi(Resource):
    def post(self):
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        user.save()
        id = user.id
        return {'id': str(id)}, 200


class LoginApi(Resource): 
    def post(self):
        body = request.get_json()
        user = User.objects.get(username=body.get('username'))
        authorized = user.check_password(body.get('password'))
        if not authorized:
            # log
            log_query = Logs(err_type="Login failed", username=body.get('username'))
            return {'error': 'Email or password invalid'}, 401

        # log
        log_query = Logs(err_type="Login Success", username=body.get('username'))

        expires = datetime.timedelta(days=7)
        access_token = create_access_token(identity=body.get('username'), expires_delta=expires)
        return {'token': access_token}, 200