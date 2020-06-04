#                                           
#       Author : wang                    
#       time   : 2020/5/31:下午11:32            
#
from flask import jsonify, Blueprint, request, current_app, render_template, flash, redirect
from flask_login import current_user

from Unless import is_isbn_or_key
from app.forms.books import SearchForms
from app.models.gift import Gift
from app.models.wish import Wish
from app.viewmodel.trade import TradeInfo
from yushu_book import YushuBook
from app.viewmodel.book import BookviewModel as vm

from app.web import web


@web.route('/book/search')
def search():
    form = SearchForms(request.args)
    if form.validate():
        q = form.q.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            res = YushuBook.search_isbn(q)
            res = vm().package_single(res, q)
        else:
            res = YushuBook.search_key(q)
            res = vm().package_collection(res, q)
    else:
        flash("搜粟不符合要求，请重新输入")
        res = None
    return render_template('search_result.html', books=res)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    book_has_gifts = False
    book_has_wishes = False

    if current_user.is_authenticated:
        if Gift.query.filter_by(isbn=isbn, launched=False, status=1).all():
            book_has_gifts = True
        if Wish.query.filter_by(isbn=isbn, launched=False, status=1).all():
            book_has_wishes = True
    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False, status=1).all()
    trade_wishs = Wish.query.filter_by(isbn=isbn, launched=False, status=1).all()
    res = YushuBook.search_isbn(isbn)

    tradeinfo_wish = TradeInfo(trade_wishs)
    tradeinfo_gift = TradeInfo(trade_gifts)
    return render_template('book_detail.html', book=res, wishes=tradeinfo_wish, gifts=tradeinfo_gift,
                           has_in_wishes=book_has_wishes
                           , has_in_gifts=book_has_gifts)
