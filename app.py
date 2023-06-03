from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sims/physics/ac-circuits')
def index():
    return render_template('ac-circuits.html')

@app.route('/sims/physics/dc-circuits')
def index():
    return render_template('dc-circuits.html')

@app.route('/sims/physics/making-waves')
def index():
    return render_template('making-waves.html')

@app.route('/sims/physics/pendulum')
def index():
    return render_template('pendulum.html')

if __name__ == '__main__':
    app.run()
