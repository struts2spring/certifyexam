import platform
 
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from src.controllers.helloController import HelloController
 
app = Flask(__name__)
 
api = Api(app)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/db/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
 
 
db = SQLAlchemy(app)
 
api.add_resource(HelloController, '/api/hello')

if __name__ == '__main__':
    print(platform.python_version())
    app.run(debug=True)