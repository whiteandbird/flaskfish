from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_required

from . import web

__author__ = '七月'

from ..models import db


from ..models.wish import Wish
from ..viewmodel.mywishes import Mywishes


@web.route('/my/wish')
def my_wish():
    wishes = Wish.get_my_wishes(current_user.id)
    isbn = []
    for x in wishes:
        isbn.append(x.isbn)
    res = Wish.get_wish_counts(isbn)
    # wishes_count = Wish.get_wish_counts(res)

    view = Mywishes(gift_mine=wishes, gifts_count=res)
    return render_template('my_wish.html', wishes=view.gifts)


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    wish = Wish()
    wish.isbn = isbn
    wish.user = current_user
    try:
        db.session.add(wish)
        db.session.commit()
    except:
        db.session.rollback()
        flash("添加成功")
    return redirect(url_for('web.search'))


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):

    form={
        'recipient_name':{'data':'aaaaaaaaaa'},
        'mobile':{'data':'12345678789'},
        'address':{'data':'湖南还僧'},
        'message':{'data':'王孙大发司法三个}'}
    }
    return render_template('drift.html', gifter=current_user, beans=current_user.beans, form=form)


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
