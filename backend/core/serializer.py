from rest_framework.serializers import ModelSerializer
from .models import Player, Gift

class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'