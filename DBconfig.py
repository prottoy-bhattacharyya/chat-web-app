import mysql.connector

def DBconfig():
  DB_CONFIG = {
    # 'host': 'localhost',
    # 'user': 'root',
    # 'password': '1234',
    # 'database': 'chat_app'

    # 'host': 'sql12.freesqldatabase.com',
    # 'user': 'sql12787491',
    # 'password': 'l3XYtyvKA6',
    # 'database': 'sql12787491'

    'host': 'mysql-938f4f6-chat-web-app.c.aivencloud.com',
    'user': 'avnadmin',
    'password': 'AVNS_RwP085SWIxjkB2CxIj5',
    'port' : '14926',
    'database': 'defaultdb'
  }
  return DB_CONFIG
