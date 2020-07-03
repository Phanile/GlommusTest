from django.shortcuts import render
from django.http import JsonResponse
from .models import Player
from .serializer import PlayerSerializer
from rest_framework.viewsets import ModelViewSet


class PlayerViewSet(ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()