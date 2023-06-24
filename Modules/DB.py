from flaskext.mysql import MySQL
from pymysql.cursors import  DictCursor

class DB(object):
    host = "localhost"
    user = "anish"
    password = "Success1@3"
    db = "db_activity"
    table = ""

    def __init__(self,app):
        app.con