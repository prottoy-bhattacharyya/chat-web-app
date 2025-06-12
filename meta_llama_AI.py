from openai import OpenAI, APIError
import DBconfig
import mysql.connector

def metaLlama(prompt, user_id, username):
    try:
      DB_CONFIG = DBconfig.DBconfig()
      sqldb = mysql.connector.connect(**DB_CONFIG)
      cursor = sqldb.cursor()
      print("Connected to database")

      cursor.execute("""SELECT api_key FROM apiKeys
                        WHERE id = 1;""")
      
      new_api_key = cursor.fetchone()[0]
      if not new_api_key:
        print("API key not found")
      
      print(f"Got API key {new_api_key}")
    except mysql.connector.Error as err:
      print(f"Error connecting to database: {err}")
      return f"database error: {err}"
      

    

    html_text = ''' Please format your response using only HTML tags. 
                          For example, use <p> for paragraphs, <strong> for bold text, 
                          <em> for italics,  
                          <br> for line breaks and colorful texts with stylish cdn tailwind css classes
                          for a white background
                          and never mention about html tags in your answer'''
    try:
      client = OpenAI(
          base_url="https://openrouter.ai/api/v1",
          api_key = new_api_key
      )

      completion = client.chat.completions.create(
          # model="meta-llama/llama-4-maverick:free",
          model = "nvidia/llama-3.1-nemotron-ultra-253b-v1:free",
          messages=[
              {
                "role": "user",
                "content": prompt + html_text
              }
            ]
      )
      response = completion.choices[0].message.content

    except APIError as err:
      return f"API error: {err}"
      
    
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
