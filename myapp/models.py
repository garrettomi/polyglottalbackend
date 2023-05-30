from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=255)
    img_url = models.CharField(max_length=255)

class Users(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Game(models.Model):
    username = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='username')
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
