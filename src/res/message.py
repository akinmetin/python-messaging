from flask import Response, request
from mongodb.models import Message, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine.queryset.visitor import Q


class PrivateMessageApi(Resource):
    @jwt_required
    def get(self, target):
        receiver = User.objects.get(username=get_jwt_identity())
        # private_messages = Message.objects.filter(sent_by=target, receiver=receiver.username).order_by('+created_at')
        private_messages = Message.objects.filter((Q(receiver__iexact=target) & Q(sent_by__iexact=receiver.username)) | (Q(receiver__iexact=receiver.username) & Q(sent_by__iexact=target))).order_by('+created_at')
        private_messages = private_messages.to_json()
        return Response(private_messages, mimetype="application/json", status=200)

    @jwt_required
    def put(self, target):
        sender = User.objects.get(username=get_jwt_identity())
        body = request.get_json()
        message_query = Message(receiver=target, message=body["message"], sent_by=sender.username)
        message_query.save()
        return '', 200


class MessageArchiveApi(Resource):
    @jwt_required
    def put(self):
        user_id = get_jwt_identity()
        body = request.get_json()
        message_query = Message(receiver=body["receiver"], message=body["message"], sent_by=user_id)
        message_query.save()
        return '', 200

    @jwt_required
    def get(self):
        username = get_jwt_identity()

        all_messages_ordered = Message.objects.filter(Q(receiver__iexact=username) | Q(sent_by__iexact=username)).order_by('+created_at')
        all_messages_ordered = all_messages_ordered.to_json()

        return Response(all_messages_ordered, mimetype="application/json", status=200)