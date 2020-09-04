from flask_restful import Resource
from Services.maps import get_xy
from flask import request

class Maps(Resource):
    def post(self):
        return {
            'status':True,
            'data': {
                'points': get_xy(request.form['gender'])
            }
        }