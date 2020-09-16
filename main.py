import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return '<h1>Hello World!</h1><a href="/teste">link</a>'

@app.route('/teste')
def teste():
  return '<h2 style="color: red;">Teste</h2>'

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)