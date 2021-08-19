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
    title=request.GET.get('title')
    order=request.GET.get('ord')
    description=request.GET.get('desc')
    response=[]

    if title=="":
        data=Api.objects.filter(movie_name__contains=title)
        data=data.order_by('movie_name')
        for i in data:
            response.append({'title':i.movie_name,'year':i.movie_year,'ratings':i.movie_rating,'duration':i.movie_duration,'description':i.movie_description })
        return HttpResponse(json.dumps(response),content_type='text/json')
    elif description=="":
        return HttpResponse("invalid description")

    elif title and order:
        if order == "movie_name" or order == "movie_rating" or order == "movie_year" or order == "movie_duration":
            data=Api.objects.filter(movie_name__contains=title)
            data=data.order_by(order)
            for i in data:
                response.append({'title':i.movie_name,'year':i.movie_year,'ratings':i.movie_rating,'duration':i.movie_duration,'description':i.movie_description })
            return HttpResponse(json.dumps(response),content_type='text/json')
        else:
           return HttpResponse("invalid order ")

    elif title:
        data=Api.objects.filter(movie_name__contains=title)
        for i in data:
            response.append({'title':i.movie_name,'year':i.movie_year,'ratings':i.movie_rating,'duration':i.movie_duration,'description':i.movie_description })
        return HttpResponse(json.dumps(response),content_type='text/json')

    elif description and order:
        if order == "movie_name" or order == "movie_rating" or order == "movie_year" or order == "movie_duration":
            data=Api.objects.filter(movie_description__contains=description)
            data=data.order_by(order)
            for i in data:
                response.append({'title':i.movie_name,'year':i.movie_year,'ratings':i.movie_rating,'duration':i.movie_duration,'description':i.movie_description })
            return HttpResponse(json.dumps(response),content_type='text/json')
        else:
            return HttpResponse("invalid order ")
    elif title and description and order:
        if order == "movie_name" or order == "movie_rating" or order == "movie_year" or order == "movie_duration":
            data=Api.objects.filter(movie_name__contains=title,movie_description__contains=description)
            data=data.order_by(order)
            for i in data:
                response.append({'title':i.movie_name,'year':i.movie_year,'ratings':i.movie_rating,'duration':i.movie_duration,'description':i.movie_description })
            return HttpResponse(json.dumps(response),content_type='text/json')
        else:
            return HttpResponse("invalid order ")

    elif description:
        data=Api.objects.filter(movie_description__contains=description)
        for i in data:
            response.append({'title':i.movie_name,'year':i.movie_year,'ratings':i.movie_rating,'duration':i.movie_duration,'description':i.movie_description })
        return HttpResponse(json.dumps(response),content_type='text/json')

    elif title and description:
        data=Api.objects.filter(movie_name__contains=title,movie_description__contains=description)
        for i in data:
            response.append({'title':i.movie_name,'year':i.movie_year,'ratings':i.movie_rating,'duration':i.movie_duration,'description':i.movie_description })
        return HttpResponse(json.dumps(response),content_type='text/json')










