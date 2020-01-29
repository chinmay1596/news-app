from django.shortcuts import render
from newsapi import NewsApiClient

def Index(request):
    newsapi = NewsApiClient(api_key='f978976b585243a2bbd4971276a07272')
    topheadlines = newsapi.get_top_headlines(sources='al-jazeera-english')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticle = articles[i]

        news.append(myarticle['title'])
        desc.append(myarticle['description'])
        img.append(myarticle['urlToImage'])

    mylist = zip(news, desc, img)

    return render(request,'index.html', context={'mylist':mylist})



def bbc(request):
    newsapi = NewsApiClient(api_key='f978976b585243a2bbd4971276a07272')
    topheadlines = newsapi.get_top_headlines(sources='bbc-news')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticle = articles[i]

        news.append(myarticle['title'])
        desc.append(myarticle['description'])
        img.append(myarticle['urlToImage'])

    mylist = zip(news, desc, img)

    return render(request,'bbc.html', context={'mylist':mylist})