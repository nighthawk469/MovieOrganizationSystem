from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

import tmdbsimple as tmdb

from start.models import Movie

tmdb.API_KEY = 'b6839ac0e265b221adb1b0d982428716'

def index(request):
	# send filter through URL (get)
	# if a sort_by GET value exists
	print(request.GET.get('sort_by'))

	if request.GET.get('sort_by') == 'rating':
		movies = Movie.objects.order_by('-average_rating') #- descending
	elif request.GET.get('sort_by') == 'release_date':
		movies = Movie.objects.order_by('-year') #- descending
	else:
		movies = Movie.objects.all()

	context = {'movies': movies}
	return render(request, 'start/index.html', context)
	# return HttpResponse("Hello, world. You're at the start index.")


def detail(request, movie_id):
	mov = Movie.objects.get(pk=movie_id)

	# use title to find poster for movies
	search = tmdb.Search()
	response = search.movie(query=mov.title)

	if len(search.results):
		path = "http://image.tmdb.org/t/p/w185" + \
			search.results[0]['poster_path']
	else:
		path = ""

	context = {'movie': mov, "path": path}
	return render(request, 'start/detail.html', context)


def blah(request):
	return HttpResponse("hello, world")
