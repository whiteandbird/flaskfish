from flask import render_template

from . import web


__author__ = '七月'

from ..models.gift import Gift


@web.route('/')
def index():
    recent_gifts = Gift.recent()
    books = [x.book for x in recent_gifts]

    return render_template('gifts.html',books=books)


@web.route('/personal')
def personal_center():
    pass
