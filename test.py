import tmdbsimple as tmdb
tmdb.API_KEY = "b6839ac0e265b221adb1b0d982428716"

def main():
	mov=tmdb.Movies(32)
	response=mov.info()
	print(mov.title)

if __name__ == '__main__':
	main()