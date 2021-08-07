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
    sources = get_news()
    print(sources)
    title = 'News Dr.'
    return render_template('index.html', title = title, sources=sources)