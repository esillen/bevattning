from flask import Flask
from valve import Valve
from database_handler import DatabaseHandler
from flask_cors import CORS
import json



app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = "localhost"
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'asdfQWER1234'
app.config['MYSQL_DATABASE_DB'] = 'bevattning'

db = DatabaseHandler(app)

CORS(app)

@app.route('/valve')
def valve_status():
    valves = db.list_valves()
    return json.dumps({'valves' : [ob.__dict__ for ob in valves]})

@app.route('/valve/<index>/action/<action>')
def valve_action(index,action):
    if action == "on":
        db.set_valve_state(index, True)
        return "Changed to on"
    elif action == "off":
        db.set_valve_state(index, False)
        return "Changed to off"
    else:
        return "Bug error crash fail"

