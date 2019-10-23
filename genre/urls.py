from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('genre/<int:genre_pk>', views.show_movies, name='movies'),
    path('movie/<int:movie_pk>', views.show_movie, name='movie'),
]