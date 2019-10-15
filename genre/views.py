from django.shortcuts import render
from .models import Genre


# Create your views here.
def index(request):
    genres = Genre.objects.all()
    return render(request, 'genre/index.html', context={'genres':genres} )
