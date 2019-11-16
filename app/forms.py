from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import User

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()]) # set to list to declare multiple validators
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators= [DataRequired()])
    email = StringField("Email", validators= [DataRequired(), Email()])
    password = PasswordField("Password", validators= [DataRequired()])
    confirm_password = PasswordField("Repeat Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")


    # custom validator for username
    def validate_username(self, username):
        user_name = User.query.filter_by(username=username.data).first()
        if user_name is not None:
            raise ValidationError("Username already exists, please use a different username")


    # custom validator for email
    def validate_email(self, email):
        user_email = User.query.filter_by(email=email.data).first()
        if user_email is not None:
            raise ValidationError("Email already exists, please use a different email")