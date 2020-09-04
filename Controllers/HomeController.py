import os
# import pandas as pd

from Config.config     import db
from flask_restful     import Resource
from flask             import request
from werkzeug.utils    import secure_filename
# from Services.submit   import allowed_file
# from Services.csvdb    import csv_to_db


class Home(Resource):
    def post(self):
        
        file = request.files['File']
        
        # if(file and allowed_file(file.filename)):
        #     filename = secure_filename(file.filename)
        #     file.save(os.path.join('../Data/', filename))
        #     csv_to_db(data=pd.read_csv("../Data/data.csv"),db=db)
        
        return {
            'status':True,
            'data'  : True
        }