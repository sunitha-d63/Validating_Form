from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, IntegerField, SubmitField
from wtforms.validators import (
    DataRequired, Length, Email, EqualTo,
    NumberRange, Regexp, Optional, ValidationError
)

def block_test_domain(form, field):
    if field.data.lower().endswith('@test.com'):
        raise ValidationError('Email from test.com is not allowed.')

def username_length(form, field):
    if len(field.data or '') <= 5:
        raise ValidationError('Username must be longer than 5 characters.')

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(message='Name is required'),
        Length(min=3, message='Name must be at least 3 characters'),
        Regexp(r'^[A-Za-z ]+$', message='Name must contain only alphabets')
    ])
    email = EmailField('Email', validators=[
        DataRequired(message='Email is required'),
        Email(message='Enter a valid email'),
        block_test_domain
    ])
    username = StringField('Username', validators=[
        DataRequired(message='Username required'),
        username_length
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message='Password is required'),
        Length(min=6, message='Password must be ≥6 chars'),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Confirm Password', validators=[
        DataRequired(message='Please confirm password')
    ])
    age = IntegerField('Age', validators=[
        DataRequired(message='Age is required'),
        NumberRange(min=18, max=60, message='Age must be between 18 and 60')
    ])
    bio = StringField('Bio (optional)', validators=[
        Optional(), Length(max=200, message='Bio cannot exceed 200 chars')
    ])
    submit = SubmitField('Register')
