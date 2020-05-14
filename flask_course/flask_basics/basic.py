from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #127.0.0.1:5000
def index():
    user_logged_in = False
    return render_template('basic.html', user_logged_in=user_logged_in)

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/information') #127.0.0.1:5000/information
def info():
    return "<h1>Puppies are cute!</h1>"

@app.route('/puppy/<name>')
def puppy(name):
    return render_template('puppy.html',name=name)

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