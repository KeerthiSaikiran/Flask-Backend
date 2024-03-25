from flask import Flask

app = Flask(__name__)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "hello Welcome"

@app.route('/<name>')
def hello_name(name):
    return 'Hello {name} !'.format(name = name)

if __name__ == '__main__':
    app.run(debug=True, port = 8081)