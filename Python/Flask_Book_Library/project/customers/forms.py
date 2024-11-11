# Form imports
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Regexp


# Flask forms (wtforms) allow you to easily create forms in this format:
class CreateCustomer(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Regexp(r'^[a-zA-Z0-9\s]+$')])
    city = StringField('City', validators=[DataRequired(), Regexp(r'^[a-zA-Z0-9\s]+$')])
    age = IntegerField('Age', validators=[DataRequired()])
    submit = SubmitField('Create Customer')
