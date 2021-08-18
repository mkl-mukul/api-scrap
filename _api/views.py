from django.shortcuts import render
from django.http import HttpResponse
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


def index(request):
    response=json.dumps([{}])
    return HttpResponse(response,content_type='text/json')

def movie(request):
    data=Api.objects.all()
    response=[{}]
    for i in data:
        response.append([{'title':i.movie_name,'year':i.movie_year,'ratings':i.movie_rating,'duration':i.movie_duration,'description':i.movie_description }])
    return HttpResponse(json.dumps(response),content_type='text/json')
    
def get_movie_id(request,r_id):
    data=Api.objects.get(id=r_id)
    response=json.dumps([{'title':data.movie_name,'year':data.movie_year,'ratings':data.movie_rating,'duration':data.movie_duration,'description':data.movie_description}])
    return HttpResponse(response,content_type='text/json')

def get_movie(request,title):
    data=Api.objects.get(movie_name=title)
    response=json.dumps([{'title':data.movie_name,'year':data.movie_year,'ratings':data.movie_rating,'duration':data.movie_duration,'description':data.movie_description}])
    return HttpResponse(response,content_type='text/json')



