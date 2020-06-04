#                                           
#       Author : wang                    
#       time   : 2020/6/2:下午3:34            
#                                           


class BookviewModel:

    def package_single(self, raw_data, keyword):
        re_dict = {}
        res = self.__cut_book_data(raw_data)
        print(res)
        re_dict['total'] = 1
        re_dict['books'] = [res]
        re_dict['keyword'] = keyword
        return re_dict

    def package_collection(self, raw_data, keyword):
        print(raw_data)
        res_dict = {
            'total': 0,
            'books': [],
            'kerword': keyword
        }

        res_dict['total'] = raw_data['total']
        res_dict['books'] = [self.__cut_book_data(book) for book in raw_data['books']]
        return res_dict

    def __cut_book_data(self, raw_data):
        book = {
            'title': raw_data['title'],
            'publisher': raw_data['publisher'],
            'pages': raw_data['pages'],
            'price': raw_data['price'],
            'author': ','.join(raw_data['author']),
            'image': raw_data['image'],
            'summary': raw_data['summary'],
            'isbn':raw_data['isbn']
        }
        return book
