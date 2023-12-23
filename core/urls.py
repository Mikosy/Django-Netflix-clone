from django.urls import path 
from . import views


app_name = 'core'

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('logout', views.logout, name="logout"),
    path('movie/<str:pk>', views.movie, name='movie'),
    path('genre/<str:pk>', views.genre, name='genre'),


    path('my-list', views.my_list, name="my-list"),
    path('add_to_list', views.add_to_list, name="add_to_list"),
    path('search', views.search, name="search"),
]
