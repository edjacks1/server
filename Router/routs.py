import sys
sys.path.append(sys.path[0] + '\..')
from Config.config import app, api
#Controllers
from Controllers.HomeController   import Home
from Controllers.GraphsController import Graphs as Graph
from Controllers.MapsController   import Maps as Map

#ROUTES
api.add_resource(Map,    '/maps'  )
api.add_resource(Graph,  '/charts')
api.add_resource(Home,   '/home'  )

application = app