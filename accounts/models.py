from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    STUDENT = 'ST'
    TEACHER = 'TE'
    
    ROLE_CHOICES = [
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
    ]
    
    role = models.CharField(max_length=2, choices=ROLE_CHOICES)
    department = models.CharField(max_length=100)
    section = models.CharField(max_length=50, blank=True, null=True)
    
    #list comprehension to create list of years 
    year = models.IntegerField(choices=[(i, f"Year {i}") for i in range(1, 5)], null=True, blank=True)  # Year field for students only

    def __str__(self):
        return self.username

