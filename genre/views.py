from django.shortcuts import render
from .models import Genre, Movie


# Create your views here.
def index(request):
    genres = Genre.objects.all()
    movies = Movie.objects.all()
    return render(request, 'genre/index.html', context={'genres':genres, 'movies':movies} )


def show_movies(request, genre_pk):
    genre = Genre.objects.get(pk=genre_pk)
    movies = Movie.objects.filter(genre=genre)
    return render(request, 'genre/movies.html', context={'movies':movies})

def show_movie(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    return render(request, 'genre/movie.html', context={'movie':movie})