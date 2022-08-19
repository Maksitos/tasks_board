from rest_framework.viewsets import ModelViewSet
from .serializers import TaskReadSerializer, UserSerializer
from ..models import Task
from django.contrib.auth.models import User




class TaskViewSet(ModelViewSet):
    serializer_class = TaskReadSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        if 'status' in self.kwargs:
            query_set = queryset.filter(status=int(self.kwargs['status']))
            return query_set
        return queryset

    
class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()