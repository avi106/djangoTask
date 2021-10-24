from django.http.response import HttpResponse
from django.shortcuts import render
# import requests
API_KEY='9660e627b6a549968c3615329ae8e186'




def say_hello(request):
    return HttpResponse("Hello World!")


# def home (request):
#     url = f'https://newsapi.org/v2/everything?q=apple&from=2021-09-23&sortBy=popularity&apiKey={API_KEY}'
#     response = requests.get(url)
#     data = response.json()
#     articles = data['articles']

#     context = {
#         'articles' : articles
#     }

#     return render(request, 'news_api/home.html', context)