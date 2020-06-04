#                                           
#       Author : wang                    
#       time   : 2020/6/3:上午8:49            
#
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError

from app.models.user import User


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64)])

    password = PasswordField(validators=[DataRequired(), Length(6, 32)])

    nickname = StringField(validators=[DataRequired(), Length(2, 10, message="必须要有两个字符，最多十个字符")])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("this email is userd")

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError("the name is used")

class LoginForm(Form):
    email = StringField(validators=[DataRequired(message="email requried"), Length(8, 64)])

    password = PasswordField(validators=[DataRequired(), Length(6, 32)])

    # nickname = StringField(validators=[DataRequired(), Length(2, 10, message="必须要有两个字符，最多十个字符")])
