#                                           
#       Author : wang                    
#       time   : 2020/6/2:下午11:01            
#
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, func
from sqlalchemy.orm import relationship

from app.models.bases import Base, db
from app.models.wish import Wish
from yushu_book import YushuBook


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # user = relationship('Book')
    # uid = Column(Integer,ForeignKey('user.id'))
    launched = Column(Boolean, default=False)

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(uid=uid, launched=False, status=1).order_by(cls.id).all()
        return gifts

    def is_your_gift(self, uid):
        return True if self.uid == uid else False

    @property
    def book(self):
        yushu = YushuBook()
        res = yushu.search_isbn(self.isbn)

        return res

    @classmethod
    def recent(cls):
        recent = Gift.query.filter_by(launched=False, status=1).group_by(cls.id).order_by(
            Gift.id).limit(5).distinct().all()
        return recent

    @classmethod
    def get_wish_counts(cls, isbn_list):
        c_list = db.session.query(func.count(Wish.id),cls.isbn).filter(Wish.launched == False, Wish.isbn.in_(isbn_list),
                                      Wish.status == 1).group_by(cls.isbn).all()
        res_list = []
        for a,b in c_list:
            res_list.append({'isbn':b, 'count':a})
        return res_list
