from rest_framework import serializers
from .models import User, Team ,User_base, Team, TeamMembership


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'display_name', 'email']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'admin', 'creation_time', 'members']




class UserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_base
        fields = ['id', 'name', 'display_name', 'creation_time']

class TeamMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMembership
        fields = ['user', 'team', 'joined_at']

class TeamSerializer(serializers.ModelSerializer):
    members = UserBaseSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'admin', 'members', 'creation_time']

# serializers.py

from rest_framework import serializers
from .models import Team, Board, Task

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name']  # Adjust fields as needed

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'  # Include all fields for now

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'  # Include all fields for now

