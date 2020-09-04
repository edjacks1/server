import sys
sys.path.insert(0, '/var/www/html/accidentes')
sys.path.insert(1, '/var/www/html/accidentes/venv/lib/python3.8/site-packages')
from Config.config  import app,api

from Controllers.HomeController   import Home
from Controllers.GraphsController import Graphs
from Controllers.MapsController   import Maps

api.add_resource(Maps,   '/maps'  )
api.add_resource(Graphs, '/charts')
api.add_resource(Home,   '/home'  )
