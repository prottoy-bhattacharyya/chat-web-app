# 💬 chat web App
**chat web App** is a real-time chat application that allows users to communicate with each other and interact with an integrated AI assistant that can answer any questions. This app uses a MySQL database for user data and chat history.

## 🚀 Features
- 🔁 Real-time chat between users

- 🤖 Integrated AI assistant for smart responses

- 🗂️ Chat history is saved in MySQL database

- 📱 Accessible in any devices connected in the same network on `port:5000`

## 🛠️ Setup Instructions
### 📌 Prerequisites
- Python 3.7+

- MySQL Server

## 📥 Installation
### 1. Clone the repository

```bash
git clone https://github.com/prottoy-bhattacharyya/Chat-web-app.git
cd Chat-web-app
```
### 2. Install Python dependencies

Make sure Python is installed: [Download Python](https://www.python.org/downloads/)
```bash
    pip install uv
```
### 3. Configure MySQL Database

First create a data base 
```bash
    CREATE DATABASE chat_app
```

Ensure MySQL is running and accessible with the following credentials:
```python
    {
        'host': 'localhost',
        'user': 'root',
        'password': '1234',
        'database': 'chat_app'
    }
```
💡 You can change these settings in your config file as needed.

### 4. Run the application

```bash
    python -m uv app.py
```
### 5. Open in your browser

```bash
    http://localhost:5000
```
### 📂 Project Structure
```csharp
|---app.py
|---meta_llama_AI.py
|---README.md
|---.gitignore
|---pyproject.toml
|---.python-version
|---uv.lock
|   
|---templates
|    |---all html pages
|--- static
    |--- all static files like images .css .js or any other
    
```
# 🧠 AI Assistant
The AI assistant is integrated into the chat window and can respond to a wide range of user queries.

# 🛡️ Security & Configuration
Ensure your MySQL root password and any sensitive environment variables are secured in production in the database. Avoid hardcoding credentials in production environments.

# 🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request for feature suggestions, bug fixes, or improvements.

# 🙋 Support
For support or questions, please open an issue in this repository.

Let me know if you'd like me to generate this as a downloadable file or add more sections like Docker support, API routes, or user authentication flow.

