from django.db import models

# Create your models here.


# model for employee
class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    address = models.TextField()
    phone = models.IntegerField()

    class Meta:
      db_table = "Employees"
    
    def __str__(self):
        return self.name


    
