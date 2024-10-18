from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    enrolled_date = models.DateField()
    teacher = models.ForeignKey(Teacher, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name