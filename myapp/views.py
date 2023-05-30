from rest_framework import generics

from .models import Pokemon, Users, Game
from .serializers import PokemonSerializer, UsersSerializer, GameSerializer


class PokemonList(generics.ListCreateAPIView):
    serializer_class = PokemonSerializer

    def get_queryset(self):
        queryset = Pokemon.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(pokemonLocation=location)
        return queryset
    
class PokemonDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()


class UsersList(generics.ListCreateAPIView):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()

class UsersDetail(generics.RetrieveDestroyAPIView):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()


class GameList(generics.ListCreateAPIView):
    serializer_class = GameSerializer
    queryset = Game.objects.all()

class GameDetail(generics.RetrieveDestroyAPIView):
    serializer_class = GameSerializer
    queryset = Game.objects.all()