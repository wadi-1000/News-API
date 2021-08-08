from flask import render_template,request,redirect,url_for
from app import app
from .request import get_news,get_articles,search_article


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

    search_article = request.args.get('article_query')

    if search_article:
        return redirect(url_for('search',source_name=search_article))
    else:
        return render_template('index.html', title = title, sources=sources)

@app.route('/article/<int:id>')
def articles(id):
    '''
    View function that returns the article details page and its data
    '''
    articles = get_articles(id)
    # title = f'{article.title}'

    return render_template('articles.html',  id = id, articles = articles)

@app.route('/search/<source_name>')
def search(source_name):
    '''
    View function to display the search results
    '''
    article_name_list = source_name.split(" ")
    artcile_name_format = "+".join(article_name_list)
    searched_articles = search_article(artcile_name_format)
    title = f'search results for {source_name}'
    return render_template('search.html', articles = searched_articles)