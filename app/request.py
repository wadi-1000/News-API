from app import app
import urllib.request,json
from .models import sources
from .models import articles

Sources = sources.Sources
Articles = articles.Articles


# Getting api key
api_key = app.config['NEWS_API_KEY']


# Getting base url
base_url = app.config['NEWS_API_BASE_URL']
articles_base_url = app.config['ARTICLES_API_BASE_URL']


def get_news():
    '''
    Function that gets json response to our url request
    '''
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    return news_results


def process_results(news_list):
    '''
    Function that processes the news result and transform them to a list of objects

    Args:
        news_list: A list of dictionaries that contain movie details

    Returns :
        news_results: A list of news objects
    '''
    news_results =[]
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')
        urlsToLogos = news_item.get('small')
        
        sources_object =Sources(id, name,description,url,category,language,country,urlsToLogos)
        news_results.append(sources_object)
        
    return news_results

def get_articles(id):
    get_articles_url = articles_base_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        articles_details_data = url.read()
        articles_details_response = json.loads(articles_details_data)

        articles_results = None

        if articles_details_response['articles']:
            articles_results_list = articles_details_response['articles']
            articles_results = process_articles(articles_results_list)
                
    return articles_results



def process_articles(articles_list):
    '''
    Function that processes articles result and transform them to a list of objects
        

    Args:
        articles_list: A list of dictionaries that contain article details

    Returns: 
        articles_results: A list of article objects
    '''
    articles_results = []
    for article_item in articles_list:
        source = article_item.get('name')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('desription')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')

        articles_object = Articles(source,author,title,description,url,urlToImage,publishedAt)
        articles_results.append(articles_object)
        
    return articles_results

def search_article(source):
    search_article_url = 'https://newsapi.org/v2/search/sources?&apiKey={}$query={}'.format(api_key,source)
    with urllib.request.urlopen(search_article_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)

        search_article_results = None

        if search_article_response['articles']:
            search_article_list = search_article_response['articles']
            search_article_results = process_search(search_article_list)

    return search_article_results