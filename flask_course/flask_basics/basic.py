from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/') #127.0.0.1:5000
def index():
    return "<h1>Hello Puppy!</h1>"

@app.route('/information') #127.0.0.1:5000/information
def info():
    return "<h1>Puppies are cute!</h1>"

@app.route('/puppy/<name>')
def puppy(name):
    return "100th letter: {}".format(name[100])

@app.route('/puppy_name/<name>')
def puppylatin(name):
    pupname = ''
    if name[-1] == 'y':
        pupname = name[:-1] + 'iful'
    else:
        pupname = name + 'y'
    return "<h1>Your puppy latin name is: {}</h1>".format(pupname)

if __name__ == '__main__':
    app.run(debug=True)