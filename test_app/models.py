from django.db import models

class User(models.Model):
    cc = models.CharField(auto_created=False, primary_key=True, serialize=False, verbose_name='CC', max_length=10)
    fullname = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=16)
    birthday = models.DateField()
    #photo
    def __str__(self):
        return self.fullname
        
    


class Company(models.Model):
    nit = models.CharField(auto_created=False, primary_key=True, serialize=False, verbose_name='NIT', max_length=9)
    name = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=15)
    address = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=30)
    objective = models.TextField()
    results = models.TextField()
    reach = models.TextField()
    state = models.TextField()
    ownerCompany = models.OneToOneField(Company, on_delete=models.CASCADE)
    def __str__(self):
        return self.objective

    
class Role(models.Model):
    rolName=models.CharField(max_length=20)
    def __str__(self):
        return self.rolName

class Roles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

class Quotation(models.Model):
    description = models.TextField()
    price = models.FloatField()
    def __str__(self):
        return self.description

class Binnacle(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Company, on_delete=models.CASCADE)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    quotation = models.OneToOneField(Quotation, on_delete=models.CASCADE)


class Meeting(models.Model):
    state = models.CharField(max_length=50)
    summary = models.TextField()
    date = models.DateField()
    binnacle = models.ForeignKey(Binnacle, on_delete=models.CASCADE)
    def __str__(self):
        return self.state