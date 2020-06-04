#                                           
#       Author : wang                    
#       time   : 2020/5/31:下午10:51            
#

def is_isbn_or_key(q):
    isbn_or_key = 'key'

    if len(q) == 13 and q.isdigit():
        isbn_or_key = 'isbn'

    elif q.replace('-', '').isdigit():
        isbn_or_key = 'isbn'

    return isbn_or_key
