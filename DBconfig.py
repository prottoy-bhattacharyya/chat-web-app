import os

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

    # 'host': 'mysql-938f4f6-chat-web-app.c.aivencloud.com',
    # 'user': 'avnadmin',
    # 'password': 'AVNS_RwP085SWIxjkB2CxIj5',
    # 'port' : '14926',
    # 'database': 'defaultdb'

    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'port' : os.getenv('DB_PORT'),
    'database': os.getenv('DB_NAME')
  }
  return DB_CONFIG
