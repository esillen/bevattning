from flask import Flask
from valve import Valve
from database_handler import DatabaseHandler
from flask_cors import CORS
import json

#################
## CREDENTIALS ##
#################
# The credentials file should have the following text:
# USERNAME = <your username>
# PASSWORD = <your password>
db_passwords_file = "db_auth.txt"
auth_data = open(db_passwords_file, "r")
auth_lines = auth_data.readlines()
auth_data = [line.split("=") for line in auth_lines]
auth_dict = dict([(item[0].strip(), item[1].strip()) for item in auth_data])

app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = "rosenhillgarden.mysql.pythonanywhere-services.com"
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = auth_dict["USERNAME"]
app.config['MYSQL_DATABASE_PASSWORD'] = auth_dict["PASSWORD"]
app.config['MYSQL_DATABASE_DB'] = 'rosenhillgarden$bevattning'

db = DatabaseHandler(app)

CORS(app)

@app.route('/valve')
def valve_status():
    valves = db.list_valves()
    return json.dumps({'valves' : [ob.__dict__() for ob in valves]})

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

