from django.db import models

class StudentModel(models.Model):
    id = models.IntegerField(primary_key = True)
    student_no = models.IntegerField()
    student_name = models.CharField(max_length=80)
    student_dob = models.DateField()
    student_doj = models.DateField()
 
    def __str__(self):
        return self.student_name


# Create your models here.
