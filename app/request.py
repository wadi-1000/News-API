from app import app
from urllib.request,json
from .models import sources

Sources = sources.Sources


# Getting api key
api_key = app.config['NEWS_API_KEY']


# Getting base url
base_url = app.config["NEWS_API_BASE_URL"]


def get_news(sources):
    '''
    Function that gets json response to our url request
    '''
    get_news_url = base_url.format(source, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['source']:
            news_results_list = get_news_response['source']
            news_results = process_results(news_results_list)

    return news_results