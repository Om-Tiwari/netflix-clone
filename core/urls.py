from django.urls import path
from . import views
app_name = 'core'

urlpatterns = [
    path('', views.index, name='netflix'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
]
