import config
import MySQLdb as mysql

class Utils(object):
    def __init__(self):
        self.conn = Utils.connect_db()

    @staticmethod
    def connect_db():
        return mysql.connect(host=config.DB_HOST, charset="utf8", connect_timeout=10, port=config.DB_PORT,
                             user=config.DB_USER, passwd=config.DB_PASSWD, db=config.DB_NAME)

    def cursor(self):
        return self.conn.cursor()


def get_conn():
    return Utils().conn