from django.db import models

# Create your models here.


#Company Model
class Company(models.Model):
    company_api = models.AutoField(primary_key= True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=50, choices = (("IT","IT"), ("Non Tech", "Non Tech"), ("other", "other")))
    added_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


#Employee Model

class Employee(models.Model):
    employee_id: models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.TextField(max_length=150);
    phone_number = models.IntegerField();
    designation = models.CharField(max_length=20,choices=(("Manager", "Manager"),("Software Developer", "SDE"),("intern","itr")))
    comapany = models.ForeignKey(Company, on_delete=models.CASCADE)