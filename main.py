from flask import Flask
from hose import Hose
from database_handler import DatabaseHandler


app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = "localhost"
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'asdfQWER1234'
app.config['MYSQL_DATABASE_DB'] = 'bevattning'

db = DatabaseHandler(app)

@app.route('/hose')
def hose_status():
    valves = db.list_valves()
    return ''.join([str(valve) for valve in valves])

@app.route('/hose/<index>/action/<action>')
def hose_action(index,action):
    if action == "on":
        db.set_valve_state(index, True)
        return "Changed to on"
    elif action == "off":
        db.set_valve_state(index, False)
        return "Changed to off"
    else:
        return "Bug error crash fail"

