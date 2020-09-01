from flask import Response, request
from mongodb.models import Message, User, Logs, Block
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine.queryset.visitor import Q
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from res.errors import SchemaValidationError, AlreadyExistsError, InternalServerError, NotExistsError


class PrivateMessageApi(Resource):
    @jwt_required
    def get(self, target):
        try:
            receiver = User.objects.get(username=get_jwt_identity())
            # private_messages = Message.objects.filter(sent_by=target, receiver=receiver.username).order_by('+created_at')
            private_messages = Message.objects.filter((Q(receiver__iexact=target) & Q(sent_by__iexact=receiver.username)) | (Q(receiver__iexact=receiver.username) & Q(sent_by__iexact=target))).order_by('-created_at')
            private_messages = private_messages.to_json()
            return Response(private_messages, mimetype="application/json", status=200)
        except DoesNotExist:
            raise NotExistsError
        except Exception:
            raise InternalServerError

    @jwt_required
    def put(self, target):
        try:
            username = get_jwt_identity()
            body = request.get_json()
            message_query = Message(receiver=target, message=body["message"], sent_by=username)
            message_query.save()
            return '', 200
        except InvalidQueryError:
            # log
            log_query = Logs(err_type="SchemaValidationError", username=username)
            log_query.save()
            raise SchemaValidationError
        except Exception:
            # log
            log_query = Logs(err_type="InternalServerError", username=username)
            log_query.save()
            raise InternalServerError


class BlockApi(Resource):
    def put(self, target):
        try:
            username = get_jwt_identity()
            
            # check for if target is already blocked
            if Block.objects.filter((Q(blocker__iexact=username) & Q(blocked__iexact=target)) | (Q(blocker__iexact=target) & Q(blocked__iexact=username))).count() >= 1:
                raise AlreadyExistsError

            block_query = Block(blocker=username, blocked=target)
            block_query.save()
            # log
            log_query = Logs(err_type="{} blocked by {}".format(target, username), username=username)
            log_query.save()
            return '', 200
        except InvalidQueryError:
            # log
            log_query = Logs(err_type="SchemaValidationError", username=username)
            log_query.save()
            raise SchemaValidationError
        except Exception:
            # log
            log_query = Logs(err_type="InternalServerError", username=username)
            log_query.save()
            raise InternalServerError


class MessageArchiveApi(Resource):
    # @jwt_required
    # def put(self):
    #     user_id = get_jwt_identity()
    #     body = request.get_json()
    #     message_query = Message(receiver=body["receiver"], message=body["message"], sent_by=user_id)
    #     message_query.save()
    #     return '', 200

    # get all messages sent from/to authenticated user
    @jwt_required
    def get(self):
        try:
            username = get_jwt_identity()
            all_messages_ordered = Message.objects.filter(Q(receiver__iexact=username) | Q(sent_by__iexact=username)).order_by('+created_at')
            all_messages_ordered = all_messages_ordered.to_json()
            # log
            log_query = Logs(err_type="Archive received", username=username)
            log_query.save()
            return Response(all_messages_ordered, mimetype="application/json", status=200)
        except DoesNotExist:
            # log
            log_query = Logs(err_type="NotExistsError", username=username)
            log_query.save()
            raise NotExistsError
        except Exception:
            # log
            log_query = Logs(err_type="InternalServerError", username=username)
            log_query.save()
            raise InternalServerError