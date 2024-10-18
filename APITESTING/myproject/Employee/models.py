from django.db import models

# Create your models here.
class Employee(models.Model):
    
    name=models.CharField(max_length=100)
    position=models.CharField(max_length=100)
    salary=models.DecimalField(max_digits=10,decimal_places =2)
    hired_date=models.DateField()


    def __str__(self):
        return self.name