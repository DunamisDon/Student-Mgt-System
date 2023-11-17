from django.db import models

# Create your models here.
class Student(models.Model):
    student_number = models.PositiveIntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    form = models.CharField(max_length=50)
    paidFees = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    