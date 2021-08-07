from flask import render_template
from app import app
from .request import get_news


#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    # Getting news sources
    news_sources = get_news('sources')
    print(news_sources)
    title = 'News Dr.'
    return render_template('index.html', title = title, sources = news_sources)