#                                           
#       Author : wang                    
#       time   : 2020/5/31:下午11:31            
#
from flask import Flask

from app.email import mail
from app.flask_log import login_manager
from app.models import init_bookdb
from app.web import web



def create_app():
    app = Flask(__name__)
    app.config.from_object('app.setting')
    app.config.from_object('app.security')
    app.register_blueprint(web)
    init_bookdb(app)
    login_manager.init_app(app)
    login_manager.login_view='web.login'
    login_manager.login_message='请先登录或者注册'
    mail.init_app(app)
    return app
