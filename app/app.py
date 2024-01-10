# Your Flask app routes
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/farmtech')
def farmtech():
    return render_template('farmtech.html')

if __name__ == '__main__':
    app.run(debug=True)
