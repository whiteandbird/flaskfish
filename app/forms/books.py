#                                           
#       Author : wang                    
#       time   : 2020/6/1:下午11:08            
#
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForms(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(1, 99)], default=1)


class DriftForm(Form):
    recipient_name = StringField('收件人姓名', validators=[DataRequired()])
    mobile = StringField("手机号", validators=[DataRequired()])
    message = StringField("留言")
    address = StringField("邮寄地址", validators=[DataRequired()])
