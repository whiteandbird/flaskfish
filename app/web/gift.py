from flask import current_app, flash, redirect, url_for, render_template

from . import web
from flask_login import login_required, current_user

from ..models import db
from ..models.gift import Gift
from ..viewmodel.mygifts import Mygifts


@web.route('/my/gifts')
@login_required
def my_gifts():
    uid = current_user.id
    print(uid)
    gifts_my_id = Gift.get_user_gifts(uid)
    isbn_list = [x.isbn for x in gifts_my_id]
    res = Gift.get_wish_counts(isbn_list)
    view = Mygifts(gift_mine=gifts_my_id, gifts_count=res)

    return render_template('my_gifts.html', gifts=view.gifts)


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        try:
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEAN_UPLOADS']
            db.session.add(gift)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
    else:
        flash("本书已经存在，请勿重复添加")
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
