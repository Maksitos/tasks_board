from rest_framework.viewsets import ModelViewSet
from .serializers import TaskAdminUpdateSerializer, TaskCreatorUpdateSerializer, TaskReadSerializer, UserSerializer, TaskWriteSerializer
from ..models import Task
from django.contrib.auth.models import User
from rest_framework.filters import SearchFilter




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
            if self.request.user == obj.creator:
                return TaskCreatorUpdateSerializer
            

            return
        return super().get_serializer_class()
    
    def perform_create(self, serializer):
        serializer.save(creator= self.request.user)

    
class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()