# we will use flask WTF forms, for our forms
# this is an extension for flask

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, SubmitField
from wtforms.validators import DataRequired

# our form used to register
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

# our form used to login
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

# our form used update login information
class UpdateForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    which = RadioField('Which', validators=[DataRequired()],
        choices=[('Piazza', 'Piazza Info'), 
            ('Gradescope', 'Gradescope Info'), ('Blackboard', 'Blackboard Info')],
        default='Piazza')
    # ('login', 'Login Info'), default='login'
    submit = SubmitField('Sign In')