from flask_restful     import Api
from flask             import Flask
from flask_sqlalchemy  import SQLAlchemy

class Config(object):
    DEBUG                          = False
    TESTING                        = False
    CSRF_ENABLED                   = True
    SECRET_KEY                     = 'miguel111'
    SQLALCHEMY_DATABASE_URI        = 'postgresql://admin:jalisco.2050@localhost/app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    
class TestingConfig(Config):
    TESTING = True

app  = Flask(__name__)
api  = Api(app)
conf = Config
app.config.from_object(conf)
db   = SQLAlchemy(app)


