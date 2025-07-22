from flask_wtf import FlaskForm
from wtforms import (
    StringField, EmailField, TextAreaField, RadioField,
    SelectField, BooleanField, PasswordField, DateField,
    IntegerField, SubmitField
)
from wtforms.validators import (
    DataRequired, Email, EqualTo, Length, NumberRange
)

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=50)], default='name')
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password', message='Passwords must match')
    ])
    gender = RadioField('Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    country = SelectField('Country', choices=[
        ('in', 'India'), ('us', 'United States'), ('uk', 'United Kingdom')
    ], default='in')
    terms = BooleanField('I accept the Terms and Conditions', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired(), Length(max=500)])
    birthdate = DateField('Birthdate', format='%Y-%m-%d', validators=[DataRequired()])
    lucky_number = IntegerField('Lucky Number', validators=[DataRequired(), NumberRange(min=1, max=100)])
    submit = SubmitField('Submit')
