from django.db import models

class Student(models.Model):
    roll_number = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.roll_number} - {self.first_name} {self.last_name}'
