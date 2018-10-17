from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, mixins, generics
from .models import Crisis
from .serializer import CrisisListSerializer, CrisisDeleteSerializer, CrisisUpdateSerializer
from .permissions import IsAuthorOrReadOnly

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

# class CrisisViewSet(viewsets.ModelViewSet):
#     """
#     处理 /api/posts/ GET POST , 处理 /api/post/<pk>/ GET PUT PATCH DELETE
#     """
#     queryset = Crisis.objects.all()
#     serializer_class = CrisisSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)

    # def perform_create(self, serializer):
    #     """
    #     重写 perform_create
    #     user 信息不在 request.data 中, 在保存时加入 user 信息
    #     """
    #
    #     serializer.save(author=self.request.user)


# class TagViewSet(mixins.CreateModelMixin,
#                  mixins.ListModelMixin,
#                  mixins.RetrieveModelMixin,
#                  viewsets.GenericViewSet):
#     """
#     处理 /api/tags/ GET POST, 处理 /api/tags/<pk>/ GET
#     """
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#
# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     处理 /api/users/ GET, 处理 /api/users/<pk>/ GET
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
class CrisisListAPIView(generics.ListAPIView):
    queryset = Crisis.objects.all()
    serializer_class = CrisisListSerializer
    permission_classes = [AllowAny]

# class CrisisCreateAPIView(generics.CreateAPIView):
#     queryset = Crisis.objects.all()
#     serializer_class = CrisisCreateSerializer
#     permission_classes = [IsAuthenticated]
#     throttle_scope = 'create_Crisis'

# class CrisisDetailAPIView(generics.RetrieveAPIView):
#     queryset = Crisis.objects.all()
#     serializer_class = CrisisDetailSerializer
#     permission_classes = [AllowAny]

class CrisisDeleteAPIView(generics.DestroyAPIView):
    queryset = Crisis.objects.all()
    serializer_class = CrisisDeleteSerializer
    permission_classes = [AllowAny]

class CrisisUpdateAPIView(generics.UpdateAPIView):
    # For now only admin can force update Crisis (change name, content, pin)
    queryset = Crisis.objects.all()
    serializer_class = CrisisUpdateSerializer
    permission_classes = [IsAdminUser]