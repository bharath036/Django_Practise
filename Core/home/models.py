from django.db import models

#Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=100)


#models.Model is a meta class as it is already predefined and modifies as per it 
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100, default='Male')
    phone_number = models.CharField(max_length=10)
    student_bio = models.TextField()

    date_of_birth = models.DateField()

    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)
