from django.shortcuts import render
from django.http import JsonResponse
from .models import Player
from .serializer import PlayerSerializer

def get_all_players(request):
    res = []
    players = Player.objects.all()
    for player in players:
        res.append(PlayerSerializer(player).data)
    return JsonResponse(res, safe = False)