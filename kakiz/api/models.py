from django.db import models

# Create your models here.
class User(models.Model):
    age=models.IntegerField()
    name=models.CharField(max_length=100)

    def __self__(self):
        return self.name
    

    