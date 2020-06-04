#                                           
#       Author : wang                    
#       time   : 2020/6/2:上午12:06            
#
import flask_sqlalchemy
from sqlalchemy import Column, Integer, String

from app.models.bases import  Base


class Book(Base):
    id = Column('id',Integer, primary_key=True, autoincrement=True)
    title = Column('title',String(50), nullable=False)
    author = Column('author',String(30), default='unknown')
    binding = Column('binding',String(20))
    publisher = Column('publisher',String(20))
    price = Column('price',String(20))
    pages = Column('pages',Integer)
    pubdate = Column('pubdate',String(20))
    isbn = Column('isbn',String(15), nullable=True, unique=True)
    summary = Column('summary',String(1000))
    imgae = Column('image',String(50))
