from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('aboutme.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/education/10')
def education10():
    return render_template('error.html')

@app.route('/education/12')
def education12():
    return render_template('error.html')

@app.route('/education/uni')
def education_uni():
    return render_template('error.html')

@app.route('/certificates')
def cerificates():
    return render_template('error.html')

@app.route('/projects')
def projects():
    return render_template('error.html')

app.run(debug=True)