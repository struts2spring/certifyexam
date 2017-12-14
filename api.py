 
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from src.controllers.helloController import HelloController
from src.service.userService import UserService
import os
 
app = Flask(__name__)
 
api = Api(app)

# print(os.environ['DATABASE_URL'])
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['HEROKU_POSTGRESQL_AQUA_URL']
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/db/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
 
 
db = SQLAlchemy(app)



 
api.add_resource(HelloController, '/api/hello')

if __name__ == '__main__':
    UserService().initDatabase()
#     print(platform.python_version())
#     print(port)
    app.run(debug=True)