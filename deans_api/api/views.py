from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, mixins, generics
from django.contrib.auth.models import User
from .models import Crisis
from .serializer import CrisisSerializer, UserSerializer
# from .serializer import CrisisListSerializer, CrisisDeleteSerializer, UserSerializer#, CrisisUpdateSerializer
from .permissions import IsAuthorOrReadOnly

from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
)


class CrisisViewSet(viewsets.ModelViewSet):
	queryset = Crisis.objects.all()
	serializer_class = CrisisSerializer

	def get_permissions(self):
		"""
		Instantiates and returns the list of permissions that this view requires.
		"""
		if self.action == 'list':
			permission_classes = [AllowAny]
		elif self.action == 'retrieve':
			permission_classes = [AllowAny]
		elif self.action == 'create':	
			permission_classes = [AllowAny]
		else:
			permission_classes = [IsAdminUser]
		return [permission() for permission in permission_classes]


# class CrisisAssistanceViewSet(viewsets.ModelViewSet):
# 	pass

# class CrisisListAPIView(generics.ListAPIView):
# 	queryset = Crisis.objects.all()
# 	serializer_class = CrisisListSerializer
# 	permission_classes = [IsAuthenticatedOrReadOnly]


# class CrisisDeleteAPIView(generics.DestroyAPIView):
# 	queryset = Crisis.objects.all()
# 	serializer_class = CrisisDeleteSerializer
# 	permission_classes = [AllowAny]

# class CrisisUpdateAPIView(generics.UpdateAPIView):
# 	# For now only admin can force update Crisis (change name, content, pin)
# 	queryset = Crisis.objects.all()
# 	serializer_class = CrisisUpdateSerializer
# 	permission_classes = [IsAdminUser]


class UserCreateView(generics.CreateAPIView):
	model = User
	permission_classes = [AllowAny]
	serializer_class = UserSerializer