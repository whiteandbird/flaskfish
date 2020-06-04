#                                           
#       Author : wang                    
#       time   : 2020/6/3:下午11:41            
#
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo


class Emailform(Form):
    email = StringField(validators=[DataRequired()])


class ResetForm(Emailform):
    password = PasswordField(validators=[DataRequired(), Length(6, 20), EqualTo('password2', message="两次密码要一置")])

    password2 = PasswordField(validators=[DataRequired(), Length(6, 20)])
