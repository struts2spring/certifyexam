from flask_restful import reqparse, abort, Api, Resource
from collections import OrderedDict
from flask_restful import fields, marshal_with
import json
from flask import jsonify, request
from flask.helpers import make_response
import pprint
import jsonpickle
from src.model.entity import User

listUser=[User(1, 'One', 'one@abc.com'),User(2, 'two', 'two@abc.com')]
userList = {
    '1':User(1, 'One', 'one@abc.com'),
    '2':User(2, 'two', 'two@abc.com'),
    }


def abortIfUserIdDoesNotExist(user_id):
    if user_id not in userList:
        abort(404, message="user_id:{} doesn't not exist".format(user_id))


parser = reqparse.RequestParser()
parser.add_argument('user')


class UserController(Resource):

    def get(self, user_id):
        abortIfUserIdDoesNotExist(user_id)
        user=userList[user_id]
        response = jsonify(jsonpickle.encode(userList[user_id], unpicklable=False))
        response.status_code = 200 # or 400 or whatever
        return response
    
    def put(self, user_id):
        args = parser.parse_args()
        json_data = request.get_json(force=True)
        user=None
#         jsonpickle.set_decoder_options('src.model.entity.User', encoding='utf8',cls=User)
        json_data.update({"py/object": "src.model.entity.User"})
        print(str(json_data))
        obj = jsonpickle.loads(str(json.dumps(json_data)))
#         obj =jsonpickle.decode(str(json_data))
        if user_id not in userList:
            userList[user_id]=obj
            user=obj
        else:
            user=userList[user_id]
        response = jsonify(jsonpickle.encode(user, unpicklable=False))
        response.status_code = 200 # or 400 or whatever
        return response

    
class UsersController(Resource):

    def get(self):
#         print(json.dumps(User(1, 'One', 'one@abc.com').__dict__))
#         resp = make_response(json.dumps(userList, default=lambda x: x.__dict__), 200)
#         pprint(json.dumps(userList))
#         jsonpickle.set_encoder_options('simplejson', sort_keys=True, indent=4)
#         jsonpickle.set_encoder_options('demjson', compactly=False)

        return jsonpickle.encode(jsonpickle.encode(listUser, unpicklable=False)), 200

    def post(self):
#         task_string = request.form['task']
#         task_db.create_task(task_string)
        return json.dumps(userList, default=lambda x: x.__dict__), 200

    def put(self, user_id):
#         todos[todo_id] = request.form['data']
        return userList

if __name__=='__main__':
    frozen=jsonpickle.encode(userList['1'], unpicklable=True)
    print(str(frozen))
#     thawed = jsonpickle.decode(frozen)
#     print(thawed)
#     print(json.dumps(userList, default=lambda x: x.__dict__))
#     print(json.dumps(userList['1'].__dict__, indent=4, cls=CustomEncoder))
