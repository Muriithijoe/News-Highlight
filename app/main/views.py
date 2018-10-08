from flask import render_template
from app import app

@app.route('/')
def index():
    message = 'News Highlight'
    return render_template('index.html',message = message)

@app.route('/news/<int:news_id>')
def news(news_id):

    return render_template('new.html', id = news_id) 
