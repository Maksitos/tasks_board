from dataclasses import field
from rest_framework import serializers
from tasks_board_app.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model= Task
        fields = '__all__'