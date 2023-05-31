from rest_framework import generics
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Pokemon, Users, Game
from .serializers import PokemonSerializer, UsersSerializer, GameSerializer
import json

@csrf_exempt
def handle_speech_recognition(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            transcript = data.get("transcript")

            if transcript:
                try:
                    correct_pokemon = Pokemon.objects.get(name__iexact=transcript)
                    return JsonResponse({"status": "success", "pokemon_name": correct_pokemon.name})
                except Pokemon.DoesNotExist:
                    all_pokemon_names = list(Pokemon.objects.values_list('name', flat=True))
                    return JsonResponse({"status": "error", "message": f"Invalid transcript: {transcript}", "all_pokemon_names": all_pokemon_names})
            else:
                return JsonResponse({"status": "error", "message": "Invalid transcript"})
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON input"})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"})


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