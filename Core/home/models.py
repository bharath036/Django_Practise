from django.db import models

#Create your models here.
class College(models.Model):
    college_name = models.CharField(max_length=100)


class Department(models.Model):
    department_name = models.CharField(max_length=100)

class Skills(models.Model):
    skill_name = models.CharField(max_length=100)


#models.Model is a meta class as it is already predefined and modifies as per it 
class Student(models.Model):
    college = models.ForeignKey(College,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100, default='Male')
    phone_number = models.CharField(max_length=10)
    student_bio = models.TextField()

    date_of_birth = models.DateField()

    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

'''

colleges = ['IIT DELHI','LPU','SRM','VIT']

departments = ['CS','IT','MECH','CIVIL'] 

skills = ['Python','English','Music','Reading']

'''
'''
student = Student.objects.create(
    name = "Akash Gupta",
    gender = "Male",
    age =  22,
    phone_number = '923348383',
    student_bio = 'Hi, I am Akash',
    email = 'akash@gmailcom',
    date_of_birth = '2020-12-11',
    college = college,
    department = department
)
'''

'''
# -------------------------------------------
# Django Models Explanation (models.py)
# -------------------------------------------
from django.db import models

# -------------------------------------------
# College Model
# -------------------------------------------
class College(models.Model):
    college_name = models.CharField(max_length=100)
    # Stores the name of the college (e.g., "IIT Delhi")

# -------------------------------------------
# Department Model
# -------------------------------------------
class Department(models.Model):
    department_name = models.CharField(max_length=100)
    # Stores the name of the department (e.g., "CS", "MECH")

# -------------------------------------------
# Skills Model
# -------------------------------------------
class Skills(models.Model):
    skill_name = models.CharField(max_length=100)
    # Stores individual skills like "Python", "Music"

# -------------------------------------------
# Student Model (Main model)
# -------------------------------------------
class Student(models.Model):
    # Foreign Key to College (One college can have many students)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    # Foreign Key to Department (One department can have many students)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    # Many-to-Many relationship with Skills (One student can have many skills and vice versa)
    skills = models.ManyToManyField(Skills)

    name = models.CharField(max_length=100)  # Student's name
    age = models.IntegerField()              # Student's age

    gender = models.CharField(max_length=100, default='Male')  # Default gender is 'Male'

    phone_number = models.CharField(max_length=10)  # Phone number as string to preserve leading zeros

    student_bio = models.TextField()  # Short student introduction or bio

    date_of_birth = models.DateField()  # DOB in YYYY-MM-DD format

    created_at = models.DateTimeField(auto_now=True)  # Automatically updates on record modification

    update_at = models.DateTimeField(auto_now_add=True)  # Set only once when the record is first created

# -------------------------------------------
# Sample Lists for Data Seeding
# -------------------------------------------
'''
'''
Predefined lists to insert via script or Django shell:

colleges = ['IIT DELHI', 'LPU', 'SRM', 'VIT']
departments = ['CS', 'IT', 'MECH', 'CIVIL']
skills = ['Python', 'English', 'Music', 'Reading']
'''

# -------------------------------------------
# Sample Object Creation (via Django shell)
# -------------------------------------------
'''
# Assuming you have created College and Department objects already:
college = College.objects.get(college_name='IIT DELHI')
department = Department.objects.get(department_name='CS')

# Creating a student
student = Student.objects.create(
    name = "Akash Gupta",
    gender = "Male",
    age =  22,
    phone_number = '923348383',
    student_bio = 'Hi, I am Akash',
    date_of_birth = '2001-12-11',
    college = college,
    department = department
)

# Adding skills to the student (after creating student)
python = Skills.objects.get(skill_name='Python')
music = Skills.objects.get(skill_name='Music')
student.skills.add(python, music)
'''

# -------------------------------------------
# Notes:
# -------------------------------------------
'''
✅ 'auto_now=True' updates field on every save
✅ 'auto_now_add=True' sets timestamp only once during creation
⚠️ Phone numbers should ideally use CharField to avoid losing leading 0s
⚠️ Always add skills after student creation due to M2M relationships
'''
