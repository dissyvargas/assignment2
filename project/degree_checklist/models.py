from django.db import models

# Create your models here.
class Student(models.Model): 
    name = models.CharField(max_length=50, help_text="Student last name, first name")
    student_id = models.IntegerField(help_text="ID number for student")

    def __str__(self):
        return self.name



class Course(models.Model): 
    completed_courses = models.TextField(help_text="Courses completed")
    required_courses = models.TextField(help_text="Courses left till graduation")
    degree_name = models.CharField(max_length=200, help_text="Student degree")

    def __str__(self):
        return self.degree_name
