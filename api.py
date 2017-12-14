import platform
 
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from src.controllers.helloController import HelloController
import os
 
app = Flask(__name__)
 
api = Api(app)
print("----------------------")
print(os.environ)
print("----------------------")
# print(os.environ['DATABASE_URL'])
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['HEROKU_POSTGRESQL_AQUA_URL']
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/db/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
 
 
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

 
api.add_resource(HelloController, '/api/hello')

if __name__ == '__main__':
    db.create_all()
    user = User('John Doe', 'john.doe@example.com')
    db.session.add(user)
    all_users = User.query.all()
    print(all_users)
    db.session.commit()
#     print(platform.python_version())
#     print(port)
    app.run(debug=True)