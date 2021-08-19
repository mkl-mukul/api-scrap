from django.db import reset_queries
from django.shortcuts import render
from django.http import HttpResponse, response
import json
from bs4 import BeautifulSoup
from .models import Api

import requests
# Create your views here.

# r = requests.get("https://www.imdb.com/chart/top?ref_=nv_mv_250")
# soup = BeautifulSoup (r.content,'lxml') 
# link_list=[]
# # links =soup.find('tbody') 
# title=soup.find_all('td',attrs = {'class':'titleColumn'})
# ratings=soup.find_all('td',attrs={'class':'ratingColumn imdbRating'})
# #data1={'title':[],'ratings':[],'year':[]}
# # for r in range(len(title)):
# #     data1['title'].append(title[r].a.text)
# #     data1['year'].append(title[r].span.text)
# #     data1['ratings'].append(ratings[r].strong.text)

# for i in range(len(title)):       
#     link_list.append(title[i].a.get('href'))
    
# #data2={'duration':[],'Description':[]}
# for i in range(len(title)):
#     r2=requests.get("https://www.imdb.com/{0}".format(link_list[i]))
#     soup2 = BeautifulSoup (r2.content,'lxml')
#     duration= soup2.find_all('li',attrs={'class':'ipc-inline-list__item'})
#     #data2['duration'].append(duration[2].text)
#     description= soup2.find('span',attrs={'class':'GenresAndPlot__TextContainerBreakpointXS_TO_M-cum89p-0 dcFkRD'})
#    # data2['Description'].append(description.text)
#     Api(movie_name=title[i].a.text,movie_year=title[i].span.text,movie_rating=ratings[i].strong.text,movie_duration=duration[2].text,movie_description=description.text).save()


def movies(request):
    response=[]
    if request.GET['title']:
        title=request.GET['title']
        data=Api.objects.filter(movie_name__contains=title)
        for i in data:
            response.append({'title':i.movie_name,'year':i.movie_year,'ratings':i.movie_rating,'duration':i.movie_duration,'description':i.movie_description })
        return HttpResponse(json.dumps(response),content_type='text/json')
    
    elif request.GET['title']=='':
        title=request.GET['title']
        data=Api.objects.all().order_by('movie_name')
        for i in data:
            response.append({'title':i.movie_name,'year':i.movie_year,'ratings':i.movie_rating,'duration':i.movie_duration,'description':i.movie_description })
        return HttpResponse(json.dumps(response),content_type='text/json')

    elif request.GET['title'] and request.GET['ord']:
        title=request.GET['title']
        ord=request.GET['ord']
        data=Api.objects.filter(movie_name__contains=title).order_by(ord)
        for i in data:
            response.append({'title':i.movie_name,'year':i.movie_year,'ratings':i.movie_rating,'duration':i.movie_duration,'description':i.movie_description })
        return HttpResponse(json.dumps(response),content_type='text/json')

    elif request.GET['title'] and request.GET['descr']:
        title=request.GET['title']
        description=request.GET['descr']
        data=Api.objects.filter(movie_name__contains=title,movie_description__contains=description)
        for i in data:
            response.append({'title':i.movie_name,'year':i.movie_year,'ratings':i.movie_rating,'duration':i.movie_duration,'description':i.movie_description })
        return HttpResponse(json.dumps(response),content_type='text/json')

    elif request.GET['title'] and request.GET['descr'] and request.GET['ord']:
        title=request.GET['title']
        description=request.GET['descr']
        ord=request.GET['ord']
        data=Api.objects.filter(movie_name__contains=title,movie_description__contains=description).all().order_by(ord)
        for i in data:
            response.append({'title':i.movie_name,'year':i.movie_year,'ratings':i.movie_rating,'duration':i.movie_duration,'description':i.movie_description })
        return HttpResponse(json.dumps(response),content_type='text/json')





