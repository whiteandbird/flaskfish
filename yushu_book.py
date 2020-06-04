#                                           
#       Author : wang                    
#       time   : 2020/5/31:下午11:19            
#
from Http import Http
from flask_restful import marshal, fields

book_fields = {
    "title":fields.String(),
}

class YushuBook:
    perpage = 15
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    key_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn.strip())
        # TODO
        # store data into sql
        res = Http.get(url)
        return res

    @classmethod
    def search_key(cls, keyword, page=1):
        url = cls.key_url.format(keyword, cls.perpage, (page - 1) * cls.perpage)
        res = Http.get(url)
        return res
