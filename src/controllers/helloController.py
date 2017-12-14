'''
Created on 14-Dec-2017

@author: vijay
'''
from flask_restful import Resource
# from src.service.userService import UserService
# from src.model.user import User
# from api import db


class HelloController(Resource):

    def get(self):
#         UserService().getUsers()
#         db.create_all()

#         all_users = User.query.all()
#         print(all_users)
        return {"response" : "hello get"} 
    
    def post(self):
        return {"response" : "hello post"}

    def put(self):
#         user = User('John Doe', 'john.doe@example.com')
#         db.session.add(user)
#         db.session.commit()
        return {"response" : "hello put"}

    def delete(self):
        return {"response" : "hello delete"}