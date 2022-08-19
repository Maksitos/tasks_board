from urllib import request
from django.contrib.auth.models import User
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..models import Task
from .permissions import IsOwnerOrAsmin, TextChangePerm, StatusChangePerm
from .serializers import (TaskAdminUpdateSerializer,
                          TaskUserUpdateSerializer, TaskReadSerializer,
                          TaskWriteSerializer, UserSerializer)


class TaskViewSet(ModelViewSet):
    serializer_class = TaskReadSerializer
    queryset = Task.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['status']

    def get_serializer_class(self):
        if self.action == 'create':
            return TaskWriteSerializer
        if self.action == 'partial_update':
            obj = self.get_object()
            if self.request.user.is_superuser:
                return TaskAdminUpdateSerializer
            else:
                return TaskUserUpdateSerializer
            
        return super().get_serializer_class()
    
    def perform_create(self, serializer):
        serializer.save(creator= self.request.user)

    def get_permissions(self):
        
        if self.action == 'create':
            self.permission_classes = [IsOwnerOrAsmin, IsAuthenticated]
        elif self.action == 'partial_update':
            self.permission_classes = [StatusChangePerm, IsAuthenticated, TextChangePerm]
        else:
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]


    
    
class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
