#                                           
#       Author : wang                    
#       time   : 2020/6/2:下午10:56            
#
import flask_sqlalchemy
from sqlalchemy import Column, SmallInteger


class Query2(flask_sqlalchemy.BaseQuery):
    def filter_by(self, **kwargs):
        kwargs['status'] = 1
        return super().filter_by(**kwargs)


db = flask_sqlalchemy.SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    status = Column(SmallInteger, default=1)

    def set_attr(self, attr_dict):
        for k, v in attr_dict.items():
            if hasattr(self, k) and k != 'id':
                setattr(self, k, v)
