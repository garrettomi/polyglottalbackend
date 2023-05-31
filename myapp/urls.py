from django.urls import path
# from .views import PokemonList, PokemonDetail, UsersList, UsersDetail, GameList, GameDetail
from . import views

urlpatterns = [
    path('pokemon/', views.PokemonList.as_view()),
    path('pokemon/<int:pk>', views.PokemonDetail.as_view()),
    path('users/', views.UsersList.as_view()),
    path('users/<int:pk>', views.UsersDetail.as_view()),
    path('game/', views.GameList.as_view()),
    path('game/<int:pk>', views.GameDetail.as_view()),
    path('speech_recognition/', views.handle_speech_recognition),
]