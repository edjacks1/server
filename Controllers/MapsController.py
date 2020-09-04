from flask_restful import Resource
from Services.maps import get_xy
from flask import request

class Maps(Resource):
    def get(self):
        return {
            'status':True,
            'data': 'hola'
            # 'data': {
            #     'points': get_xy(request.form['gender'])
            # }
        }