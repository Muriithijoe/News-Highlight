from flask import render_template
from . import main
from .. model import Source
from ..request import get_sources, get_articles


@main.route('/')
def index():
    message = 'News Highlight'
    return render_template('index.html',message = message)

@main.route('/news/<int:news_id>')
def news(news_id):

    return render_template('news.html',  )
