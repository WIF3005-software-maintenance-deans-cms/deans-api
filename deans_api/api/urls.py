from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from .views import (
    CrisisViewSet,
    CrisisAssistanceViewSet,
    CrisisTypeViewSet,
    CrisisUpdateView,
    CrisisPartialUpdateView,
    UserViewSet,
    UserPartialUpdateView,
    EmergencyAgenciesView,
    EmergencyAgenciesPartialUpdateView,
    SiteSettingViewSet,
)

# Define the router for ViewSets
router = DefaultRouter()
router.register(r'crises', CrisisViewSet)
router.register(r'crisisassistance', CrisisAssistanceViewSet)
router.register(r'crisistype', CrisisTypeViewSet)
router.register(r'users', UserViewSet)
router.register(r'emergencyagencies', EmergencyAgenciesView)
router.register(r'sitesettings', SiteSettingViewSet)

# Define urlpatterns
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('', include(router.urls)),  # Include all ViewSet-based routes
    path('crises/update/<int:pk>/', CrisisUpdateView.as_view(), name='crisis_update'),
    path('crises/update-partial/<int:pk>/', CrisisPartialUpdateView.as_view(), name='crisis_partial_update'),
    path('users/update-partial/<int:pk>/', UserPartialUpdateView.as_view(), name='user_partial_update'),
    path('emergencyagencies/update-partial/<int:pk>/', EmergencyAgenciesPartialUpdateView.as_view(), name='emergencyagency_partial_update'),
]
