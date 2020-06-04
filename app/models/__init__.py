#                                           
#       Author : wang                    
#       time   : 2020/6/2:上午12:06            
#
import flask


from app.models.bases import db




def init_bookdb(app: flask.Flask):
    db.init_app(app)
    db.create_all(app=app)


if __name__ == '__main__':
    qu = Query()
    qu.filter_by(name='wang',age=1)