from . import models 

def genre_variable(request):
    genres = models.Genre.objects.all()
    return {
        'genres':genres
    }