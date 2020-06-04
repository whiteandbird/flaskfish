#                                           
#       Author : wang                    
#       time   : 2020/6/3:下午12:56            
#
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, func
from sqlalchemy.orm import relationship

from app.models.bases import Base, db
from yushu_book import YushuBook


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)


    @classmethod
    def get_my_wishes(cls,uid):
        res =  Wish.query.filter_by(uid=uid,status=1,launched=False).order_by(
            cls.id
        ).all()
        return res

    @property
    def book(self):
        yushu = YushuBook()
        res = yushu.search_isbn(self.isbn)
        return res

    @classmethod
    def recent(cls):
        recent = Wish.query.filter_by(launched=False, status=1).group_by(cls.id).order_by(
            cls.id).limit(5).distinct().all()
        return recent

    @classmethod
    def get_wish_counts(cls, isbn_list):
        c_list = db.session.query(func.count(Wish.id), cls.isbn).filter(Wish.launched == False,
                                                                        Wish.isbn.in_(isbn_list),
                                                                        Wish.status == 1).group_by(cls.isbn).all()
        res_list = []
        for a, b in c_list:
            res_list.append({'isbn': b, 'count': a})
        return res_list
