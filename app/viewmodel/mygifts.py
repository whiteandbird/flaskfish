#                                           
#       Author : wang                    
#       time   : 2020/6/3:下午9:37            
#


class Mygifts:
    def __init__(self, gift_mine, gifts_count):
        self.gifts = []
        self.gifts_mine = gift_mine
        self.gifts_count = gifts_count
        self.__parse()

    def __parse(self):

        for gift in self.gifts_mine:
            count = 0
            for ct in self.gifts_count:
                if gift.isbn == ct['isbn']:
                    count=ct['count']
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










