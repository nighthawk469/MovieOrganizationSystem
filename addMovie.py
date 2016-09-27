#tmdb API used (python2 only)
#https://pypi.python.org/pypi/tmdb3/

import os, sys, django

print("Authenticating API_KEY on tmdb.com...")
import tmdbsimple as tmdb
tmdb.API_KEY = "b6839ac0e265b221adb1b0d982428716"

#sets the DJANGO_SETTINGS_MODULE environment variable, which gives Django 
#the python import path to your mysite/settings.py file
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OrganizationSystem.settings")
django.setup()

from start.models import Movie



#try, if movie doesn't exist, HTTPError
titleList = []

def addById(idist):

	# add 5 movies to django database using tmdb3 api information
	for i in idist:

		# tmdb3
		# m = Movie(title=mov.title, year=mov.releasedate.strftime("%Y"), director=mov.crew[0].name, average_rating=mov.userrating, plot_description=mov.tagline)

		# tmdbsimple
		mov = tmdb.Movies(int(i))
		response = mov.info()

		# keep track of the titles
		titleList.append(mov.title)

		title = mov.title
		year = mov.release_date[:4]
		rating = mov.vote_average
		overview = mov.overview

		response = mov.credits()
		director = mov.crew[0]["name"]

		m = Movie(title=title, year=year, director=director, average_rating=rating, plot_description=overview)
		m.save()

def main():
	print("Enter a command (search, addId, addName):")
	cmd = input()
	if cmd == "addId":
		print("Enter movie ids, seperated by a space")
		ids = input()
		idList = ids.split()
		addById(idList)
		print(*titleList, sep="") #shortcut for printing a list

	sys.exit()

if __name__ == '__main__':
	main()
