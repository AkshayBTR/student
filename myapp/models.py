from django.db import models

# Create your models here.
class Student_Details(models.Model):
    USN=models.CharField(max_length=10,unique=True)
    Phno=models.CharField(max_length=10,primary_key=True)
    Name=models.CharField(max_length=30)
    Email=models.EmailField(unique=True)
    Percentage=models.DecimalField(max_digits=4,decimal_places=2)
    YOP=models.CharField(max_length=4)

    def __str__(self):
        return self.USN
    