#                                           
#       Author : wang                    
#       time   : 2020/6/3:下午9:37            
#
from collections import namedtuple

# Mygift = namedtuple('Mygift',['id','book','wishes_count'])

class Mywishes:
    def __init__(self, gift_mine, gifts_count):
        self.gifts = []
        self.gifts_mine = gift_mine
        self.gifts_count = gifts_count
        self.__parse()

    def __parse(self):

        for gift in self.gifts_mine:
            print(gift.__dict__)
            count = 0
            for ct in self.gifts_count:
                print('====',ct)
                if gift.isbn == ct['isbn']:
                    count=ct['count']
            print(gift.book)
            r = {
                'wishes_count':count,
                'book':gift.book,
                'id':gift.id
            }
            self.gifts.append(r)






# class Mygift:
#     def __init__(self):
#         pass
#










