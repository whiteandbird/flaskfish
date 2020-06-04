#                                           
#       Author : wang                    
#       time   : 2020/6/2:下午10:56            
#
from math import floor

from flask import current_app
from sqlalchemy import Column, Integer, Boolean, Float, String
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import Serializer
from Unless import is_isbn_or_key
from app.enums import PendingStatus
from app.models.bases import Base, db
from flask_login.mixins import UserMixin

from app.models.drift import Drift
from app.models.gift import Gift
from app.models.wish import Wish
from yushu_book import YushuBook


class User(UserMixin, Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column('nickname', String(25), nullable=False)
    phone_number = Column(String(30), unique=True)
    _password = Column('password', String(100), nullable=False)
    email = Column(String(20), unique=True, nullable=True)
    confirmes = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    recive_counter = Column(Integer, default=0)
    isbn = Column(String(15), nullable=True, unique=True)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    def check_password(self, raw_password):
        if check_password_hash(self._password, raw_password):
            return True
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return "{} {} {} {}".format(self.nickname, self.email, self.beans, self.send_counter)

    def can_save_to_list(self, isbn):
        if is_isbn_or_key(isbn) != 'isbn':
            return False
        yushu = YushuBook()
        if not yushu.search_isbn(isbn):
            return False

        gift = Gift.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        wish = Wish.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        if not gift and not wish:
            return True
        return False

    def generate_token(self, expire=600):
        secret_key = current_app.config.get('SECRET_KEY')

        s = Serializer(secret_key, str(expire))
        temp = s.dumps({'id': self.id})
        return temp

    def can_send_drift(self):
        if self.beans<1:
            return False
        success_gift_count = Gift.query.filter_by(uid=self.id,launched=False, status=1).count()
        success_receive_count = Drift.query.filter_by(requester_id=self.id, pending=PendingStatus.success.value).count()

        return True if floor(success_receive_count/2)<= floor(success_gift_count) else False

    @property
    def summary(self):
        return dict(
            nickname=self.nickname,
            beans = self.beans,
            email = self.email,
            send_receive=str(self.send_counter)+'/'+str(self.recive_counter)
        )

def reset_password(token, newpassword):
    s = Serializer(current_app.config["SECRET_KEY"], str(600))
    try:
        data = s.loads(token)
    except:
        return False
    else:
        uid = data.get('id')
        user = User.query.get(uid)
        user.password = newpassword

        try:
            db.session.add(user)
            db.session.commit()
        except:
            db.rollback()
            return False
        return True
