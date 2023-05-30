from django.urls import path
from .views import PokemonList, PokemonDetail, UsersList, UsersDetail, GameList, GameDetail

urlpatterns = [
    path('pokemon/', PokemonList.as_view()),
    path('pokemon/<int:pk>', PokemonDetail.as_view()),
    path('users/', UsersList.as_view()),
    path('users/<int:pk>', UsersDetail.as_view()),
    path('game/', GameList.as_view()),
    path('game/<int:pk>', GameDetail.as_view()),
]