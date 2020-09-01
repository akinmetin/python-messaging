from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from decouple import config

from mongodb.db import initialize_db
from flask_restful import Api
from res.routes import initialize_routes
from res.errors import errors


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# mongodb env vars
app.config['MONGODB_SETTINGS'] = {
    "db": config("DB_NAME"),
    "host": config("DB_HOST"),
    "port": int(config("DB_PORT")),
    "username": config("DB_USER"),
    "password": config("DB_PASSWORD"),
    "authentication_source": "admin"
}


initialize_db(app)
initialize_routes(api)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)