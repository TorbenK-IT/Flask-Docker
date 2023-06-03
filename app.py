from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sims/physics/ac-circuits')
def ac_circuits():
    return render_template('ac-circuits.html')

@app.route('/sims/physics/dc-circuits')
def dc_circuits():
    return render_template('dc-circuits.html')

@app.route('/sims/physics/making-waves')
def making_waves():
    return render_template('making-waves.html')

@app.route('/sims/physics/pendulum')
def pendulum():
    return render_template('pendulum.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')