from flask_wtf import FlaskForm
from wtforms import ( StringField, PasswordField, 
                     SelectMultipleField, SubmitField, BooleanField)
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from ceevee_backend.models.role import Role

class RegisterForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    roles = SelectMultipleField("Roles", coerce=int, validators=[DataRequired()], 
                                choices=[(role.id, role.name) for role in Role.query.all()])
    submit = SubmitField("SignUp")

    def validate_email(self, email):
        """Validate users email"""
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Please try another email")



class LoginForm(FlaskForm):
    """ Login form"""
    email = StringField("Email", validators=[DataRequired(), Length(min=2, max=20)])
    password = password = PasswordField("Password", validators=[DataRequired()])
    rememberMe = BooleanField("Remember Me")
    submit = SubmitField("Login")
