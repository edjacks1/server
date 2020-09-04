import sys
sys.path.insert(0, '/var/www/html/accidentes')
sys.path.insert(1, '/var/www/html/accidentes/venv/lib/python3.8/site-packages')
from Router.routs   import aplication
from flask_restful  import Api

from Controllers.HomeController   import Home
from Controllers.GraphsController import Graphs
from Controllers.MapsController   import Maps

#ROUTES
api  = Api(aplication)

api.add_resource(Maps,   '/maps'  )
api.add_resource(Graphs, '/charts')
api.add_resource(Home,   '/home'  )
