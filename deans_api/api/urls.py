from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from rest_framework import routers

from .views import (
    CrisisViewSet
)

router = routers.DefaultRouter()
router.register(r'crises', CrisisViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]