from flask import Flask, render_template, request
from weather import Weather

app = Flask(__name__)
app.secret_key = '0647'

@app.route('/')
def homepage():
    day_weather = Weather()
    day_weather.single_day_weather('London')
    return render_template('index.html', content=day_weather.get_data())

@app.route('/search')
def search():
    city = request.args.get('city').title()
    day_weather = Weather()
    day_weather.single_day_weather(city)
    return render_template('index.html', content=day_weather.get_data())

app.run(port=6047)
