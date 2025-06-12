import mysql.connector

def DBconfig():
  DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234',
    'database': 'chat_app'
  }
  return DB_CONFIG