from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=255, unique=True)
    img_url = models.URLField(null=True)

    class Meta:
        app_label = 'myapp'

    def __str__(self):
        return self.name

class Users(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Game(models.Model):
    username = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='username')
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
