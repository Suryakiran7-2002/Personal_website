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
    return render_template('10th.html')

@app.route('/education/12')
def education12():
    return render_template('12th.html')

@app.route('/education/uni')
def education_uni():
    return render_template('uni.html')

@app.route('/certificates')
def cerificates():
    return render_template('certificates.html')

@app.route('/certificates/courses')
def cerificates_c():
    return render_template('courses.html')

@app.route('/certificates/hackathons')
def cerificates_h():
    return render_template('hackathons.html')

@app.route('/certificates/workshops')
def cerificates_w():
    return render_template('error.html')

@app.route('/projects')
def projects():
    return render_template('error.html')

if __name__ == '__main__':
    app.run()