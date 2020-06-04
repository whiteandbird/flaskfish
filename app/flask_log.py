#                                           
#       Author : wang                    
#       time   : 2020/6/3:上午11:57            
#

from app.models.user import User
from flask_login import LoginManager

login_manager = LoginManager()


@login_manager.user_loader
def uer_loader(userid):
    return User.query.get(userid)


@login_manager.user_loader
def get_user(userid):
    return User.query.get(userid)