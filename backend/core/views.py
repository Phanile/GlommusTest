from django.shortcuts import render
from django.http import JsonResponse
from .models import Player

def get_all_players(request):
    players = Player.objects.all().values()
    return JsonResponse(list(players), safe = False)