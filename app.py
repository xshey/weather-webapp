from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from weather import Weather
from form import SearchForm

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.secret_key = '0647'

@app.route('/', methods=['POST', 'GET'])
def homepage():
    day_weather = Weather()
    form = SearchForm()
    if form.is_submitted():
        city = form.search_term.data
    else:
        city = 'London'
    day_weather.single_day_weather(city)
    return render_template('index.html', content=day_weather.get_data(), form=form)


@app.errorhandler(404)
def page_not_found():
    pass

@app.errorhandler(500)
def server_error():
    pass

app.run(port=6047)
