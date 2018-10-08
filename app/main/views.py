from flask import render_template
from . import main
from .. model import Source
from ..request import get_sources, get_articles


@main.route('/')
def index():
    sources = get_sources()
    print(sources)
    message = 'News Highlight'
    return render_template('index.html',message=message, sources=sources)

@main.route('/news/<int:id>')
def news(id):
    articles = get_articles(id)
    print(articles)


    return render_template('news.html',news=articles, name='News Highlight')
