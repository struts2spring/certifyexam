'''
Created on 14-Dec-2017

@author: vijay
'''
from api import db
from src.model.user import User

class UserService():
    
    def getUsers(self):
        
        print('getUsers')
    
    def createDatebase(self):
        db.create_all()
        
    def addUsers(self):
        user = User('John Doe', 'john.doe@example.com')
        db.session.add(user)
        db.session.commit()

    def initDatabase(self):
        self.createDatebase()
        self.addUsers()
        
if __name__ == '__main__':
    UserService().initDatabase()
    
    pass