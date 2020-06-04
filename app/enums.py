#                                           
#       Author : wang                    
#       time   : 2020/6/4:下午2:06            
#
from enum import Enum


class PendingStatus(Enum):
    waitting = 1
    success = 2
    reject = 3
    redraw = 4


if __name__ == '__main__':
    a =  PendingStatus.success
    print(111)