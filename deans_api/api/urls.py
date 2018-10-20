from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from rest_framework import routers

from .views import (
    CrisisViewSet,
    UserCreateView
)

router = routers.DefaultRouter()
router.register(r'crises', CrisisViewSet)
# router.register(r'CrisisAssistance',)

urlpatterns = [
	path('api-auth/', include('rest_framework.urls')),
	path('register/', UserCreateView.as_view(), name='user-register'),
	# path('crises/', CrisisListAPIView.as_view(), name='user-list'),
    url(r'^', include(router.urls)),
]