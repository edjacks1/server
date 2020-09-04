import sys
sys.path.remove('/usr/local/lib/python38.zip')
sys.path.remove('/usr/local/lib/python3.8')

sys.path.insert(0, '/var/www/html/accidentes')
sys.path.insert(1, '/var/www/html/accidentes/venv/lib/python3.8/site-packages')
from Router.routs import application
