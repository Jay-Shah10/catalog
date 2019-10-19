from django.shortcuts import render
from .models import Genre, Movie


# Create your views here.
def index(request):
    genres = Genre.objects.all()
    return render(request, 'genre/index.html', context={'genres':genres} )

def show_movies(request, pk):
    genre = Genre.objects.get(pk=pk)
    movies = Movie.objects.filter(genre=genre)
    return render(request, 'genre/movies.html', context={'movies':movies})
