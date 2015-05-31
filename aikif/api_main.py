# api_main.py

from flask import Flask, jsonify, abort, make_response
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from flask.ext.httpauth import HTTPBasicAuth

app = Flask(__name__, static_url_path="")
api = Api(app)
auth = HTTPBasicAuth()

app.config['BASIC_AUTH_USERNAME'] = 'local'
app.config['BASIC_AUTH_PASSWORD'] = 'local'

base_url = '/aikif/api/v1.0/'    # http://127.0.0.1:5000/aikif/api/v1.0/facts/2
base_url = '/aikif/api/v2.0/'
base_url = '/'                   # http://127.0.0.1:5000/facts/2
url_pre = 'http://127.0.0.1:5000' 
#basic_auth = BasicAuth(app)



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

help_fields = {
    'help_id': fields.String,
    'help_str': fields.String,
    'help_url': fields.String
} 
  
help_list = [
    {
        'help_id': 'help',
        'help_str': 'Returns list of all API commands (No authentication needed)',
        'help_url': url_pre + base_url + 'help'
    },
    {
        'help_id': 'log',
        'help_str': 'Log events',
        'help_url': url_pre + base_url + 'log'
    },
    {
        'help_id': 'users',
        'help_str': 'List all the users of the system',
        'help_url': url_pre + base_url + 'users'
    },
    {
        'help_id': 'facts',
        'help_str': 'Facts contain raw strings added by users',
        'help_url': url_pre + base_url + 'facts'

    }
]


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

fact_fields = {
    'fact_id':  fields.String,
    'fact_str': fields.String
}

users = [
    {
        'user_id':1,
        'username':'local',
        'password':'local'
    },
    {
        'user_id':2,
        'username':'guest',
        'password':'guest'
    }
]   
 
user_fields = {
    'user_id':  fields.String,
    'username': fields.String,
    'password': fields.String
}

logs = [
    { 'txt':'First default log entry' },
    { 'txt':'Second default log entry' },
    { 'txt':'Third and last log entry' }
 ]
    

log_fields = {
    'txt': fields.String
}


map_fields = {
    'map_id':  fields.String,
    'map_name': fields.String
}

maps = [
    { 'map_id':1, 'map_name':'map test1' },
    { 'map_id':2, 'map_name':'map test2' }
 ]

class HelpListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('help_str', type=str, required=True,
                                   help='No Help content provided',
                                   location='json')
        super(HelpListAPI, self).__init__()

    def get(self):
        return {'help': [marshal(h, help_fields) for h in help_list]}


class FactListAPI(Resource):
    #decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('fact_str', type=str, required=True,
                                   help='No Fact content provided',
                                   location='json')
        super(FactListAPI, self).__init__()

    def get(self):
        return {'facts': [marshal(fact, fact_fields) for fact in facts]}

    def post(self):
        args = self.reqparse.parse_args()
        fact = {
            'fact_id': facts[-1]['fact_id'] + 1,
            'fact_str': args['fact_str']
        }
        facts.append(fact)
        return {'fact': marshal(fact, fact_fields)}, 201
        
    def put(self, fact_id):
        fact = [fact for fact in facts if fact['fact_id'] == fact_id]
        if len(fact) == 0:
            abort(404)
        fact = fact[0]
        args = self.reqparse.parse_args()
        for k, v in args.items():
            if v is not None:
                fact[k] = v
        return {'fact': marshal(fact, fact_fields)}

    def delete(self, fact_id):
        fact = [fact for fact in facts if fact['fact_id'] == fact_id]
        if len(fact) == 0:
            abort(404)
        facts.remove(fact[0])
        return {'result': True}
    
class FactAPI(Resource):
    #decorators = [auth.login_required]
    
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('fact_id', type=str, location='json')
        self.reqparse.add_argument('fact_str', type=str, location='json')
        super(FactAPI, self).__init__()
    
    def get(self, fact_id):
        #fact =[fact for fact in facts if fact['fact_id'] == fact_id]
        for fact in facts:
            if fact['fact_id'] == fact_id:
                return {'fact':marshal(fact, fact_fields)}
        abort(404)

class UserAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('user_id',  type=str, location='json')
        self.reqparse.add_argument('username', type=str, location='json')
        self.reqparse.add_argument('password', type=str, location='json')
        super(UserAPI, self).__init__()
        
    def get(self, user_id):
        for user in users:
            if user['user_id'] == user_id:
                return {'user':marshal(user, user_fields)}
        abort(404)

    def put(self, user_id):
        pass

    def delete(self, user_id):
        pass

import aikif.cls_log as mod_log
import aikif.config as mod_cfg

class MapperListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('map_id',  type=str, location='json')
        self.reqparse.add_argument('map_name',  type=str, location='json')
        super(MapperListAPI, self).__init__()
        
    def get(self):
        return {'maps': [marshal(map, map_fields) for map in maps]}

    def post(self, map_id, map_name):
        print('Mapper put: adding mapping ' + txt)
        args = self.reqparse.parse_args()

        map = {
            'map_id':  args['map_id'],
            'map_name':  args['map_name'],
        }
        return {'map': marshal(map, map_fields)}, 201


class LogAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('txt',  type=str, location='json')
        self.lg = mod_log.Log(mod_cfg.fldrs['log_folder'])
        super(LogAPI, self).__init__()
        

    def post(self, txt):
        print('Log put: recording event ' + txt)
        self.lg.record_process(txt)
        args = self.reqparse.parse_args()

        log = {
            'txt':  args['txt']
        }
        return {'log': marshal(log, log_fields)}, 201
        
        
api.add_resource(HelpListAPI, base_url + 'help',                endpoint = 'help')
api.add_resource(LogAPI,      base_url + 'log/<string:txt>',    endpoint = 'log')
api.add_resource(LogAPI,      base_url + 'logs',    endpoint = 'logs')
api.add_resource(UserAPI,     base_url + 'users/<int:user_id>', endpoint = 'user')
api.add_resource(FactListAPI, base_url + 'facts',               endpoint = 'facts')
api.add_resource(FactAPI,     base_url + 'facts/<int:fact_id>', endpoint = 'fact')
api.add_resource(MapperListAPI, base_url + 'maps',               endpoint = 'maps')

if __name__ == '__main__':
    app.run(debug=True)
    