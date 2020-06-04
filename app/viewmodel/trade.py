#                                           
#       Author : wang                    
#       time   : 2020/6/3:下午3:37            
#                                           

class TradeInfo:
    def __init__(self, good):
        self.total = 0
        self.trades = []
        self.__parse(good)

    def __parse(self, good):
        self.total = len(good)
        self.trades = [self.__map_to_dict(x) for x in good]

    def __map_to_dict(self, single):
        return dict(
            username=single.user.nickname,
            id=single.id
        )
