from .message import PrivateMessageApi, MessageArchiveApi
from .auth import SignupApi, LoginApi

def initialize_routes(api):
    api.add_resource(PrivateMessageApi, '/api/message/<target>')
    api.add_resource(MessageArchiveApi, '/api/message/archive')

    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')