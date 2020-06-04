#                                           
#       Author : wang                    
#       time   : 2020/6/4:上午10:20            
#                                           


from flask_mail import Message, Mail

mail = Mail()

def send_message():
    msg = Message(subject='test', sender="2714269544@qq.com",body="test2",
                  recipients=["1096576877@qq.com"])
    mail.send(msg)