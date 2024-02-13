# Your Flask app routes
from flask import Flask, render_template, url_for


app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('index.html')

#Backend code for Dashboard page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

#Backend code for Services page
@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/suitable_market')
def suitable_market():
    return render_template('suitable_market.html')

@app.route('/crop_recommendation')
def crop_recommendation():
    return render_template('crop_recommendation.html')
@app.route('/disease_identification')
def disease_identification():
    return render_template('disease_identification.html')

@app.route('/fertilizer_recommendation')
def fertilizer_recommendation():
    return render_template('fertilizer_recommendation.html')
@app.route('/check_weather')
def check_weather():
    return render_template('check_weather.html')


#Backend code for News page
@app.route('/news')
def news():
    return render_template('news.html')

#Backend code for Connect page
@app.route('/connect')
def connect():
    return render_template('connect.html')

#Backend code for Farmtech page
@app.route('/farmtech')
def farmtech():
    return render_template('farmtech.html')

#Backend code for Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


#Backend code for Register page
@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


#Backend code for Help page
@app.route('/help')
def help():
    return render_template('help.html')

if __name__ == '__main__':
    app.run(debug=True)
