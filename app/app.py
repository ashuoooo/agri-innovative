# Your Flask app routes
from flask import Flask, render_template, url_for


app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/services')
def services():
    return render_template('services.html')
@app.route('/check_weather')
def check_weather():
    return render_template('check_weather.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/farmtech')
def farmtech():
    return render_template('farmtech.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
