from django.db import models
class user(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def _str_(self):
        return self.username 
        


# Create your models here.
