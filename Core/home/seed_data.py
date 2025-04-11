#For adding data to database.
from .models import * 
from faker import Faker
import random 

fake = Faker()
# college = College.objects.all().order_by('?')[0]  #means order by anything randomly not particular order, 0 means fist

def seedDB(num_records=10): 
    for record in range(0,num_records):
        college = College.objects.all().order_by('?')[0]
        department = Department.objects.all().order_by('?')[0]
        skills = Skills.objects.all().order_by('?')
        name = fake.name()
        age = random.randint(18,34)
        genders = ['Male','Female']
        gender = random.choices(genders)
        phone_number = random.randint(10000000,9999999999)
        student_bio = fake.sentence()
        date_of_birth = fake.date()
        created_at = fake.date()
        student = Student.objects.create(
            college = college ,
            department =  department, 
            name = name ,
            gender = gender, 
            age = age , 
            phone_number = phone_number,
            student_bio = student_bio,
            date_of_birth = date_of_birth,
            created_at = created_at
            )
        for skill in skills[:2]:
            student.skills.add(skill)
            student.save()

#After writting this functions go to shell and see it's working or not

'''
-->python manage.py shell 
--> In future we will see bulk create in which we can pass fake data in minimal time
'''

'''
# ------------------------------
# Django Seed Script Explanation
# Purpose: Populate the database with fake student data for testing/development
# ------------------------------

# Import all models from current app
from .models import *  

# Import Faker for generating dummy data
from faker import Faker  

# Import random module for generating random values
import random  

# Instantiate the Faker object
fake = Faker()

# ------------------------------
# Function to seed database
# num_records: number of student records to insert
# ------------------------------
def seedDB(num_records=10):  
    for record in range(0, num_records):

        # Randomly select a college from all existing colleges
        college = College.objects.all().order_by('?')[0]

        # Randomly select a department from all existing departments
        department = Department.objects.all().order_by('?')[0]

        # Get all available skills in a random order
        skills = Skills.objects.all().order_by('?')

        # Generate fake name using Faker
        name = fake.name()

        # Generate a random age between 18 and 34
        age = random.randint(18, 34)

        # Randomly select a gender from the list
        genders = ['Male', 'Female']
        gender = random.choices(genders)  # ⚠️ This returns a list, not a string. Should use random.choice()

        # Generate a random 9 or 10-digit phone number
        phone_number = random.randint(10000000, 9999999999)

        # Generate a short random sentence as student bio
        student_bio = fake.sentence()

        # Generate a random birth date
        date_of_birth = fake.date()

        # Generate a random date for created_at (e.g., registration date)
        created_at = fake.date()

        # Create a new student record in the DB
        student = Student.objects.create(
            college=college,
            department=department,
            name=name,
            gender=gender,  # ⚠️ If using random.choices(), fix it with gender=gender[0]
            age=age,
            phone_number=phone_number,
            student_bio=student_bio,
            date_of_birth=date_of_birth,
            created_at=created_at
        )

        # Assign top 2 random skills to the student (many-to-many field)
        for skill in skills[:2]:
            student.skills.add(skill)
            student.save()  # Not necessary to save in each loop; could move out for performance

# ------------------------------
# HOW TO USE THIS FUNCTION IN DJANGO SHELL
# ------------------------------
'''

'''
Step-by-step:

1. Open Django shell:
    python manage.py shell

2. Import and run the function:
    from yourapp.seed_script import seedDB
    seedDB(20)  # Adds 20 random student entries

Notes:
- You can increase the number of records by changing the argument.
- In production, use bulk_create for efficiency if adding many records.
- Always ensure you have data in College, Department, and Skills tables before running.
'''

# ------------------------------
# Recommendations:
# ------------------------------
'''
✅ Use random.choice() instead of random.choices() for a single gender value:
   gender = random.choice(genders)

✅ Consider moving student.save() outside the for loop when adding skills

✅ Optionally add logging or print statements to confirm progress
'''