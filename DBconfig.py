import mysql.connector

def DBconfig():
  DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234',
    'database': 'test_chat_app'
  }
  return DB_CONFIG