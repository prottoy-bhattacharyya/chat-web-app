from openai import OpenAI, APIError, RateLimitError, APIConnectionError
import DBconfig
import mysql.connector
import requests


def metaLlama(prompt, user_id, username):
    try:
      DB_CONFIG = DBconfig.DBconfig()
      sqldb = mysql.connector.connect(**DB_CONFIG)
      cursor = sqldb.cursor()
      print("Connected to database")
      
    test_webhook_url = "http://localhost:5678/webhook-test/test-webhook"
    prod_webhook_url = "http://localhost:5678/webhook/test-webhook"

    try:
      user_id = str(user_id)
      url = prod_webhook_url + "?prompt=" + prompt +  "&sessionID=" + user_id
      response = requests.get(url)
      if response.status_code == 200:
          response = response.json()
          response = str(response[0].get("output"))
    except Exception as e:
      return f"Error processing API request: {e}"
      
    try:
      cursor.execute('''INSERT INTO aiChat(user_id, username, prompt, response)
                      VALUES(%s, %s, %s, %s)''',
                    (int(user_id), username, prompt, response))
      sqldb.commit()

    except mysql.connector.Error as err:
      return f"database error: {err}"
    finally:
      cursor.close()
      sqldb.close()
      
    return response
