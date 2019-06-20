from valve import Valve
from flaskext.mysql import MySQL

class DatabaseHandler:

    def __init__(self, app):
        mysql = MySQL()
        mysql.init_app(app)
        self.connection = mysql.connect()
        self.cur = self.connection.cursor()

    def list_valves(self):
        self.cur.execute("SELECT ID, State FROM Valves")
        result = self.cur.fetchall()
        valves = [Valve(data[0], state = data[1]) for data in result]
        return valves
    
    def set_valve_state(self, index, new_state):
        self.cur.execute("UPDATE Valves SET State = %s WHERE Id=%s", (new_state, index))

    def __del__(self):
        self.cur.close()
        connection.close()

