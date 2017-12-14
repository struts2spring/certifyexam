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
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/db/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
 
 
db = SQLAlchemy(app)
 
api.add_resource(HelloController, '/api/hello')

if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    port = int(os.environ.get('PORT', 5000)) 
#     print(platform.python_version())
#     print(port)
    app.run(host='0.0.0.0', port=port, debug=False)