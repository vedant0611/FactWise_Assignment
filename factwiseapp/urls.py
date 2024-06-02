from django.urls import path
from .views import CreateTeamView, ListTeamsView, RetrieveUpdateDestroyTeamView, AddUsersToTeamView, RemoveUsersFromTeamView, ListTeamUsersView,CreateUserView, ListUsersView, DescribeUserView, UpdateUserView, GetUserTeamsView

urlpatterns = [
    path('create_team/', CreateTeamView.as_view(), name='create-team'),
    path('list_teams/', ListTeamsView.as_view(), name='list-teams'),
    path('team/<int:team_id>/', RetrieveUpdateDestroyTeamView.as_view(), name='team-detail'),
    path('team/<int:team_id>/add_users/', AddUsersToTeamView.as_view(), name='add-users-to-team'),
    path('team/<int:team_id>/remove_users/', RemoveUsersFromTeamView.as_view(), name='remove-users-from-team'),
    path('team/<int:team_id>/list_users/', ListTeamUsersView.as_view(), name='list-team-users'),


    path('create_user/', CreateUserView.as_view(), name='create_user'),
    path('list_users/', ListUsersView.as_view(), name='list_users'),
    path('describe_user/', DescribeUserView.as_view(), name='describe_user'),
    path('update_user/', UpdateUserView.as_view(), name='update_user'),
    path('get_user_teams/', GetUserTeamsView.as_view(), name='get_user_teams'),

]


