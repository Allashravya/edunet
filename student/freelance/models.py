from django.db import models
class login(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)

    def __str__(self):
            return self.username
    def __str__(self):
          return self.password
class register(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)

    def __str__(self):
            return self.username
    def __str__(self):
          return self.email
    def __str__(self):
          return self.password
class freelance(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

# Create your models here.
