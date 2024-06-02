# api/models.py

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    display_name = models.CharField(max_length=100)
    email = models.EmailField()

class Team(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=128)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User, related_name='teams')




from django.db import models

class User_base(models.Model):
    name = models.CharField(max_length=64, unique=True)
    display_name = models.CharField(max_length=64)
    creation_time = models.DateTimeField(auto_now_add=True)

class Team(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    admin = models.ForeignKey(User_base, related_name='admin_teams', on_delete=models.CASCADE)
    members = models.ManyToManyField(User_base, related_name='teams', through='TeamMembership')
    creation_time = models.DateTimeField(auto_now_add=True)

class TeamMembership(models.Model):
    user = models.ForeignKey(User_base, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)





    def __str__(self):
        return self.name


