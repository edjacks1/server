import sys
sys.path.append(sys.path[0] + '\..')
from Config.config import app, api
#Controllers
from Controllers.HomeController   import Home
from Controllers.GraphsController import Graphs
from Controllers.MapsController   import Maps

#ROUTES
api.add_resource(Maps,   '/map'  )
api.add_resource(Graphs, '/chart')
api.add_resource(Home,   '/homes'  )

application = app