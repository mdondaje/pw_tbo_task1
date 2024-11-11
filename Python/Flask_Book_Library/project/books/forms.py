# Form imports
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Regexp


# Flask forms (wtforms) allow you to easily create forms in format:
class CreateBook(FlaskForm):
    name = StringField('Book Name', validators=[DataRequired(), Regexp(r'^[a-zA-Z0-9\s]+$')])
    author = StringField('Author', validators=[Regexp(r'^[a-zA-Z0-9\s]+$')])
    year_published = IntegerField('Year Published', validators=[DataRequired()])
    book_type = SelectField('Book Type', choices=[('2days', 'Up to 2 days'), ('5days', 'Up to 5 days'), ('10days', 'Up to 10 days')], validators=[DataRequired()])
    submit = SubmitField('Create Book')
