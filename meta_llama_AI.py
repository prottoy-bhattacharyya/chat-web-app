from openai import OpenAI, APIError
import DBconfig
def metaLlama(prompt, user_id, username):
    DB_CONFIG = DBconfig.DBconfig()
    sqldb = mysql.connector.connect(**DB_CONFIG)
       
    cursor = sqldb.cursor()

    html_text = ''' Please format your response using only HTML tags. 
                          For example, use <p> for paragraphs, <strong> for bold text, 
                          <em> for italics,  
                          <br> for line breaks and colorful texts
                          and never mention about html tags in your answer'''

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key= "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"
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
    try:
      response = completion.choices[0].message.content
    except APIError as err:
      if err.status_code == 401:
        return "please provide the correct api key"
      else:
        return f"API Error: {err}"
    
    try:
      cursor.execute('''INSERT INTO aiChat(user_id, username, prompt, response)
                      VALUES(%s, %s, %s, %s)''',
                    (int(user_id), username, prompt, response))
      sqldb.commit()

    except Error as err:
      return f"database error: {err}"
    finally:
      cursor.close()
      sqldb.close()
      
    return response
