from flask import flash, redirect, url_for, render_template, request
from flask_login import login_required, current_user
from sqlalchemy import or_

from . import web

__author__ = '七月'

from ..forms.books import DriftForm
from ..models.drift import Drift

from ..models.gift import Gift
from ..viewmodel.drift import DriftCollection


@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
@login_required
def send_drift(gid):
    gift = Gift.query.get(gid)
    if gift:
        if gift.is_your_gift(current_user.id):
            flash("此书是你自己的书阿！！！！！！")
            return redirect(url_for('web.book_detail', isbn=gift.isbn))
        can = current_user.can_send_drift()
        if not can:
            return render_template('not_enough_beans.html', beans=current_user.beans)

        form = DriftForm(request.args)
        if request.method.lower() == 'post' and form.validate():
            save_drift(form, gift)
        gifter = gift.user.summary

        return render_template('drift.html', gifter=gifter, user_beans=current_user.beans, form=form)


@web.route('/pending')
@login_required
def pending():
    drift = Drift.query.filter(or_(Drift.requester_id == current_user.id, Drift.gifter_id == current_user.id)).all()
    view = DriftCollection(drift, current_user.id)
    return render_template('pending.html', drifts=view.data)


@web.route('/drift/<int:did>/reject')
def reject_drift(did):
    pass


@web.route('/drift/<int:did>/redraw')
def redraw_drift(did):
    pass


@web.route('/drift/<int:did>/mailed')
def mailed_drift(did):
    pass


def save_drift(drift_form, current_gift):
    dift = Drift()
    # dift.message = drift_form.message.data
    drift_form.populate_obj(dift)
    dift.gift_id = current_gift.id
    dift.requester_id = current_user.id
    dift.requester_nickname = current_user.nickname
    dift.gifter_nickname = current_gift.nickname
    dift.gifter_id = current_gift.id

    book = current_gift.book
    dift.book_title = book.get('title')
    dift.book_author = book.get('author')
    dift.book_img = book.get('image')
    dift.isbn = book.get('isbn')

    current_user.beans -= 1
