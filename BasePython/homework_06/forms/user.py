from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    name = StringField('Full Name', name="name", validators=[
        DataRequired()
    ])
    username = StringField('Username', name="username", validators=[
        DataRequired()
    ])
    email = StringField('Email', name="email", validators=[
        DataRequired()
    ])