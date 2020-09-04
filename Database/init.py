import sys
sys.path.append(sys.path[0] + '/..')
from Config.config    import app,db
from flask_script     import Manager
from flask_migrate    import Migrate, MigrateCommand
from Models           import accident,accident_type,affected,brand,car,car_type,cause,detail,municipality,neighborhood,place,route,street,subbrand

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.run()