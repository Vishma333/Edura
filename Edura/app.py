from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/mou')
def mou():
    return render_template('mou.html')

@app.route('/placement')
def placement():
    return render_template('placement.html')

@app.route('/departments')
def departments():
    return render_template('departments.html')

@app.route('/payments')
def payments():
    return render_template('payments.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')


if __name__ == '__main__':
    app.run(debug=True)
