from dataclasses import field
from email.policy import default
from rest_framework import serializers
from tasks_board_app.models import Task
from django.contrib.auth.models import User


class TaskReadSerializer(serializers.ModelSerializer):
    creator = serializers.CharField(source='creator.username')
    performer = serializers.CharField(source='performer.username', allow_null=True)
    class Meta:
        model= Task
        fields = ['creator', 'performer', 'time', 'text']


class TaskWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Task
        fields = ['performer', 'text']


class TaskCreatorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Task
        fields = ['text']


class TaskAdminUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Task
        fields = ['performer', 'text']



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'username'