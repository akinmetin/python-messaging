from flask import Response, request
from flask_jwt_extended import create_access_token
from mongodb.models import User, Logs
from flask_restful import Resource
import datetime
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist
from res.errors import SchemaValidationError, AlreadyExistsError, UnauthorizedError, InternalServerError


class SignupApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user = User(**body)
            user.hash_password()
            user.save()
            # id = user.id
            Response("success", mimetype="application/json", status=200)
            # return {'id': str(id)}, 200
        except FieldDoesNotExist:
            # log
            log_query = Logs(err_type="SchemaValidationError", username='None')
            log_query.save()
            raise SchemaValidationError
        except NotUniqueError:
            # log
            log_query = Logs(err_type="AlreadyExistsError", username='None')
            log_query.save()
            raise AlreadyExistsError
        except Exception:
            # log
            log_query = Logs(err_type="InternalServerError", username='None')
            log_query.save()
            raise InternalServerError


class LoginApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user = User.objects.get(username=body.get('username'))
            authorized = user.check_password(body.get('password'))
            if not authorized:
                # log
                log_query = Logs(err_type="Login failed", username=body.get('username'))
                log_query.save()
                raise UnauthorizedError
                # return {'message': 'Email or password invalid'}, 401

            # log
            log_query = Logs(err_type="Login success", username=body.get('username'))
            log_query.save()

            expires = datetime.timedelta(days=7)
            access_token = create_access_token(identity=body.get('username'), expires_delta=expires)
            return {'token': access_token}, 200
        except (UnauthorizedError, DoesNotExist):
            # log
            log_query = Logs(err_type="InternalServerError", username=body.get('username'))
            log_query.save()
            raise UnauthorizedError
        except Exception:
            # log
            log_query = Logs(err_type="InternalServerError", username=body.get('username'))
            log_query.save()
            raise InternalServerError
