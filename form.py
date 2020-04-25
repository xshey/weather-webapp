from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    search_term = StringField('City:', validators=[DataRequired()])
    submit = SubmitField('Search')
