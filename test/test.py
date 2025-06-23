from flask import Flask, render_template, request
import mysql.connector

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234',
    'database': 'chat_app'
  }

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        folder = "static/"
        name = "1.jpg"
        file.save(folder + name)
    return render_template('uploadImg.html')

if __name__ == '__main__':
    app.run(debug=True)