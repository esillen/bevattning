from flask import Flask, render_template, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import datetime
import json
import os
from os.path import expanduser
home = expanduser("~")
basepath = os.path.join(home, "github", "bevattning", "backend")

DATA_UPLOAD_INTERVAL_SECONDS = 60 * 5 # The worker data update frequency
SAVED_HISTORY_SECONDS = 60 * 60 * 12 # Save 12h history
MAX_MI_FLORA_DATAPOINTS = SAVED_HISTORY_SECONDS / DATA_UPLOAD_INTERVAL_SECONDS # Save this many datapoints

#################
## CREDENTIALS ##
#################
# The credentials file should have the following text:
# USERNAME = <your username>
# PASSWORD = <your password>
db_passwords_file = os.path.join(basepath, "db_auth.txt")
auth_data = open(db_passwords_file, "r")
auth_lines = auth_data.readlines()
auth_data = [line.split("=") for line in auth_lines]
auth_dict = dict([(item[0].strip(), item[1].strip()) for item in auth_data])

frontendpath = os.path.join(basepath, "..", "frontend", "app")

app = Flask(__name__, static_folder=os.path.join(frontendpath, "build", "static"), template_folder=os.path.join(frontendpath, "build"))

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{hostname}/{databasename}".format(
    username=auth_dict["USERNAME"],
    password=auth_dict["PASSWORD"],
    hostname=auth_dict["HOSTNAME"],
    databasename=auth_dict["DATABASE"],
)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

CORS(app)

# Yes I should be imported here (and not before) because reasons
from valve import Valve
from mi_flora_datapoint import MiFloraDatapoint
from health import Health
from settings import Settings

try:
    MiFloraDatapoint.__table__.drop(db.engine) # Begin by dropping the table, we'll recreate it in the next step
except:
    print ("mi flora datpoints table doesn't exist")
try:
    Health.__table__.drop(db.engine)
except:
    print ("health  table doesn't exist")

db.create_all()
health = Health(last_access = datetime.datetime.utcnow())# Create the first (and only) entry
db.session.add(health)
db.session.commit()

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/valve')
def valve_status():
    valves = Valve.query.all()
    return json.dumps({'valves' : [ob.as_dict() for ob in valves]})

@app.route('/valve/<id>', methods=['POST'])
def valve_action(id):
    password = request.json['password']
    server_password = Settings.query.filter_by(key="password").first().value
    if password == server_password:
        valve = Valve.query.filter_by(id=id).first()
        action = request.json['action']
        if valve == None:
            "valve index out of range"
        else:
            if action == "on":
                valve.state = True
                valve.last_opened = datetime.datetime.utcnow()
                db.session.commit()
                return "Changed to on"
            elif action == "off":
                valve.state = False
                valve.last_closed = datetime.datetime.utcnow()
                db.session.commit()
                return "Changed to off"
            else:
                return "bad action"
    else:
        return "bad password", 401 #sure I'll fix a better response code once I know this works


@app.route('/miflora', methods=['GET', 'POST'])
def miflora():
    if request.method == 'POST':
        mi_flora_datapoint = MiFloraDatapoint(jsonBlob = json.dumps(request.json))
        db.session.add(mi_flora_datapoint)
        db.session.commit()
        datapoints = MiFloraDatapoint.query
        if datapoints.count() > MAX_MI_FLORA_DATAPOINTS:
            db.session.delete(datapoints[0])
            db.session.commit()
        return "ok"
    elif request.method == 'GET':
        mi_flora_datapoints = MiFloraDatapoint.query.all()
        return json.dumps([json.loads(ob.jsonBlob) for ob in mi_flora_datapoints]) 

@app.route('/health', methods=['GET', 'POST'])
def health():
    if request.method == 'POST':
        health = Health.query.first()
        health.last_access = datetime.datetime.utcnow()
        db.session.commit()
        return 'ok'
    elif request.method == 'GET':
        health = Health.query.first()
        return json.dumps(health.as_dict())
