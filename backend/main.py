from flask import Flask, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import datetime
import json
import os
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

basepath = auth_dict["WORKINGDIR"]
frontendpath = os.path.join(basepath, "..", "frontend", "app")

print (frontendpath)
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

db.create_all()

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/valve')
def valve_status():
    valves = Valve.query.all()
    return json.dumps({'valves' : [ob.as_dict() for ob in valves]})

@app.route('/valve/<id>/action/<action>')
def valve_action(id, action):
    valve = Valve.query.filter_by(id=id).first()
    print(valve)
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
            db.session.commit()
            return "Changed to off"
        else:
            return "bad action"

