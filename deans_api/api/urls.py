from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from rest_framework import routers

from .views import (
    CrisisViewSet,
    CrisisAssistanceViewSet,
    CrisisTypeViewSet,
    UserViewSet
)

router = routers.DefaultRouter()
router.register(r'crises', CrisisViewSet)
router.register(r'crisisassistance', CrisisAssistanceViewSet)
router.register(r'crisistype', CrisisTypeViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
	path('api-auth/', include('rest_framework.urls')),
    url(r'^', include(router.urls)),
]