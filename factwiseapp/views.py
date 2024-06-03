from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Team, User_base, TeamMembership
from .serializers import UserSerializer, TeamSerializer, UserBaseSerializer, TeamMembershipSerializer
import json


class CreateTeamView(APIView):
    
        def post(self, request):
            print(request.data)
            serializer = TeamSerializer(data=request.data)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListTeamsView(APIView):
    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

class RetrieveUpdateDestroyTeamView(APIView):
    def get(self, request, team_id):
        try:
            team = Team.objects.get(id=team_id)
            serializer = TeamSerializer(team)
            return Response(serializer.data)
        except Team.DoesNotExist:
            return Response({'error': 'Team does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, team_id):
        try:
            team = Team.objects.get(id=team_id)
            serializer = TeamSerializer(instance=team, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Team.DoesNotExist:
            return Response({'error': 'Team does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, team_id):
        try:
            team = Team.objects.get(id=team_id)
            team.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Team.DoesNotExist:
            return Response({'error': 'Team does not exist'}, status=status.HTTP_404_NOT_FOUND)

class AddUsersToTeamView(APIView):
    def put(self, request, team_id):
        user_ids = request.data.get('users', [])
        if not user_ids:
            return Response({'error': 'User IDs not provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            team = Team.objects.get(id=team_id)
            for user_id in user_ids:
                try:
                    user = User.objects.get(id=user_id)
                    team.members.add(user)
                except User.DoesNotExist:
                    return Response({'error': f'User with ID {user_id} does not exist'}, status=status.HTTP_404_NOT_FOUND)
            return Response({'message': 'Users added to team successfully'})
        except Team.DoesNotExist:
            return Response({'error': 'Team does not exist'}, status=status.HTTP_404_NOT_FOUND)

class RemoveUsersFromTeamView(APIView):
    def put(self, request, team_id):
        user_ids = request.data.get('users', [])
        if not user_ids:
            return Response({'error': 'User IDs not provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            team = Team.objects.get(id=team_id)
            for user_id in user_ids:
                try:
                    user = User.objects.get(id=user_id)
                    team.members.remove(user)
                except User.DoesNotExist:
                    return Response({'error': f'User with ID {user_id} does not exist'}, status=status.HTTP_404_NOT_FOUND)
            return Response({'message': 'Users removed from team successfully'})
        except Team.DoesNotExist:
            return Response({'error': 'Team does not exist'}, status=status.HTTP_404_NOT_FOUND)

class ListTeamUsersView(APIView):
    def get(self, request, team_id):
        try:
            team = Team.objects.get(id=team_id)
            users = team.members.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        except Team.DoesNotExist:
            return Response({'error': 'Team does not exist'}, status=status.HTTP_404_NOT_FOUND)

class CreateUserView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        serializer = UserBaseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"id": serializer.data['id']}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListUsersView(APIView):
    def get(self, request):
        users = User_base.objects.all()
        serializer = UserBaseSerializer(users, many=True)
        return Response(serializer.data)

class DescribeUserView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        user_id = data.get('id')
        try:
            user = User_base.objects.get(id=user_id)
            serializer = UserBaseSerializer(user)
            return Response(serializer.data)
        except User_base.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

class UpdateUserView(APIView):
    def put(self, request):
        data = json.loads(request.body)
        user_id = data.get('id')
        user_data = data.get('user')
        if 'name' in user_data:
            return Response({'error': 'User name cannot be updated'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User_base.objects.get(id=user_id)
            serializer = UserBaseSerializer(instance=user, data=user_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User_base.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

class GetUserTeamsView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        user_id = data.get('id')
        try:
            user = User_base.objects.get(id=user_id)
            teams = user.teams.all()
            serializer = TeamSerializer(teams, many=True)
            return Response(serializer.data)
        except User_base.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

from .models import Team, Board, Task
from .serializers import TeamSerializer, BoardSerializer, TaskSerializer

class CreateBoardView(APIView):
    def post(self, request):
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
