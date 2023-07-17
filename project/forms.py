from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import NumberRange, InputRequired


class HomeForm(FlaskForm):
    height = IntegerField('высота мира', validators=[InputRequired('input height'), NumberRange(min=5, max=100, message="diap height")])
    width = IntegerField('ширина мира', validators=[InputRequired("input height"), NumberRange(min=5, max=100, message="diap widht")])
    submit = SubmitField("Submit")
