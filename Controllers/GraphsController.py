from flask_restful     import Resource
from Services.charts   import gender, month, hour, age, car_type, cause, injured
from flask import request

class Graphs(Resource):
    def get(self):
        return {
            'status': True,
            'data': {'gender':gender(),
                    'month':month(),
                    'hour':hour(),
                    'age':age(),
                    'car_type':car_type(),
                    'cause':cause(),
                    'injured':injured()}
        }
    def post(self):
        gen = request.form['gender']
        return {
            'status': True,
            'data': {
                    'month':month(gen),
                    'hour':hour(gen),
                    'age':age(gen),
                    'car_type':car_type(),
                    'cause':cause(gen),
                    'injured':injured(gen),
                    'gender':gender()}
            }