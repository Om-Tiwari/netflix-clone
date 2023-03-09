from django.urls import path
from .views import *
app_name = 'core'

urlpatterns = [
    path('', index, name='netflix'),
    path('signin', signin, name='signin'),
    path('signup', signup, name='signup'),
    path('signout', signout, name='signout'),
    path('watch',Watch.as_view(),name='watch'),
    path('movie/detail/<str:movie_id>/',ShowMovieDetail.as_view(),name='show_det'),
    path('movie/play/<str:movie_id>/',ShowMovie.as_view(),name='play')
]
