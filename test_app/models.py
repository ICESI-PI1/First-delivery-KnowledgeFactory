from django.db import models

# Create your models here.

#En todas las llaves foráneas se puede hacer "on_delete=CASCADE", decidan a cuales se les pone

class Users(models.Model):
    name = models.CharField(max_length=200)
    cc = models.BigAutoField(auto_created=False, primary_key=True, serialize=False, verbose_name='CC')
    email = models.EmailField()
    password = models.CharField(max_length=16)
    phoneNumber = models.CharField(max_length=10)
    birthDay = models.DateField()
    photo = models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)
    #binnacleId = models.ForeignKey(Binnacle)


class Company(models.Model):
    nit = models.BigAutoField(auto_created=False, primary_key=True, serialize=False, verbose_name='NIT')
    phoneNumber = models.CharField(max_length=10)
    address = models.CharField(max_length=300)
    name = models.CharField(max_length=50)
    user_cc = models.ForeignKey(Users, on_delete=models.CASCADE)


class Project(models.Model):
    idProject = models.BigAutoField(auto_created=False, primary_key=True, serialize=False, verbose_name='ID')
    objective = models.TextField()
    results = models.TextField()
    reach = models.TextField()
    state = models.TextField()
    company_nit = models.ForeignKey(Company, on_delete=models.CASCADE)
    
class Meet(models.Model):
    state = models.CharField(max_length=40)
    summary = models.TextField()
    date = models.DateField()
    #binnacleId = models.ForeignKey(Binnacle) 
    
class Binnacle(models.Model):
    projectId = models.ForeignKey(Project, on_delete=models.CASCADE)
    quoteId = models.ForeignKey(Meet, on_delete=models.CASCADE)
    user_cc = models.ForeignKey(Users, on_delete=models.CASCADE)
    
class Quotation(models.Model):
    price = models.FloatField()
    description = models.TextField()
    user_cc = models.ForeignKey(Users, on_delete=models.CASCADE)
    binnacleId = models.ForeignKey(Binnacle, on_delete=models.CASCADE)
    
class Role(models.Model):
    rolName = models.CharField(max_length=50)
    

class Roles(models.Model):
    userId = models.CharField(max_length=100)
    roleId = models.ForeignKey(Role, on_delete=models.CASCADE)
    user_cc = models.ForeignKey(Users, on_delete=models.CASCADE)