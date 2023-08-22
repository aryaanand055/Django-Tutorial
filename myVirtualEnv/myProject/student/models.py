from django.db import models


# Create your models here.
class Student(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    phone = models.IntegerField()
    dob = models.DateField(null=True)

    # For the name to be displayed in the admin view in the webpage
    def __str__(self):
        return f"{self.fname} {self.lname}"
