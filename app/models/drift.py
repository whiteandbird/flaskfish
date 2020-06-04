#                                           
#       Author : wang                    
#       time   : 2020/6/4:下午1:45            
#
from sqlalchemy import Column, Integer, String, SmallInteger

from app.models.bases import Base


class Drift(Base):
    id = Column(Integer,primary_key=True)
    recipient_name = Column(String(20), nullable=True, default="aa@qq.com")
    address = Column(String(100), nullable=False)
    message = Column(String(200))
    mobile = Column(String(20),nullable=False)

    isbn = Column(String(13))
    book_title = Column(String(50))
    book_author = Column(String(30))
    book_img = Column(String(50))

    requester_id = Column(Integer)
    requester_nickname = Column(String(20))

    gifter_id = Column(Integer)
    gift_id = Column(Integer)
    gifter_nickname = Column(String(20))

    pending = Column('pending', SmallInteger, default=1)
