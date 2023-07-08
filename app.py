from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    host_url = os.getenv('HOST_URL')
    return f'Hello, World! URL is {host_url}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')