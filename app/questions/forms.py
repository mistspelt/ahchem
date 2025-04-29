from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import InputRequired, NumberRange

class RecordMarksForm(FlaskForm):
    marks = IntegerField('Marks', validators=[InputRequired(), NumberRange(min=0)])
    submit = SubmitField('Save')