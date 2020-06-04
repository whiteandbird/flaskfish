#                                           
#       Author : wang                    
#       time   : 2020/6/4:下午3:51            
#
import datetime


class DriftCollection:
    def __init__(self, drift, current_user_id):
        self.data = []
        self.__parse(drift, current_user_id)

    def __parse(self, drift, current_user_id):
        for d in drift:
            temp = DriftView(d, current_user_id)
            self.data.append(temp.data)


class DriftView:
    def __init__(self, drift, current_user_id):
        self.data = {}
        self.data = self.__parse(drift)

    def __parse(self, d):
        time = datetime.datetime.now()
        r = {
            'you_are': 'gifter',
            'drift_id': d.id,
            'book_title': d.book_title,
            'book_author': d.book_author,
            'book_img': d.book_img,
            'date': time.strftime("%Y-%m-%d"),
            'message': d.message,
            'operator': 'wwwwww',
            'status_str': 'sending',
            'address': d.address,
            'recipient_name': d.recipient_name,
            'mobile': d.mobile,
            'status': d.pending
        }
        return r
