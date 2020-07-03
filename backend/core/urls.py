from django.contrib import admin
from django.urls import path
from .views import PlayerViewSet
from rest_framework.routers import SimpleRouter, DefaultRouter

router = DefaultRouter()
router.register("players", PlayerViewSet)

urlpatterns = router.urls
