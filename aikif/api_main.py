# api_main.py

from flask import Flask, jsonify, abort, make_response
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from flask.ext.httpauth import HTTPBasicAuth

app = Flask(__name__, static_url_path="")
api = Api(app)
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'local':
        return 'local'
    return None

@auth.error_handler
def unauthorized():
    # return 403 instead of 401 to prevent browsers from 
    # displaying the default auth dialog
    return make_response(jsonify({'message':'Unauthorized access'}), 403)

facts = [
    {
        'fact_id':1,
        'fact_str':'A Project is a process using resources',
    },
    {
        'fact_id':2,
        'fact_str':'AIKIF is a Project',
    }
]
    
class FactAPI(Resource):
    decorators = [auth.login_required]
    
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('fact_id', type=str, location='json')
        self.reqparse.add_argument('fact_str', type=str, location='json')
        super(FactAPI, self).__init__()
    
    def get(self, fact_id):
        fact =[f for f in facts if f['fact_id'] == fact_id]
        if len(fact) == 0:
            abort(404)
        return {'fact':marshal(fact[0], fact_fields)}


if __name__ == '__main__':
    app.run(debug=True)
    