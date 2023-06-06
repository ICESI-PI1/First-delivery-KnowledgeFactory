from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomUserManager(BaseUserManager): 
    def _create_user(self, email, password, fullname, cc, birthday, phoneNumberU,**extra_fields) :
        if not email: 
            raise ValueError("Debe incluir un email")
        if not password: 
            raise ValueError("Debe incluir un password")
        
        user = self.model(
            email=self.normalize_email(email), 
            fullname = fullname, 
            cc = cc, 
            birthday = birthday, 
            phoneNumberU = phoneNumberU, 
            **extra_fields
        )

        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_user(self, email, password, fullname, cc, birthday, phoneNumberU,**extra_fields) :
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, fullname, cc, birthday, phoneNumberU,**extra_fields)

    def create_superuser(self, email, password, fullname, cc, birthday, phoneNumberU,**extra_fields) :
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, fullname, cc, birthday, phoneNumberU,**extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    cc = models.CharField(auto_created=False, primary_key=True, serialize=False, verbose_name='CC', max_length=10)
    fullname = models.CharField(max_length=50)
    phoneNumberU = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, verbose_name="email", unique=True)
    password = models.CharField(max_length=100)
    birthday = models.DateField()
    
    is_staff = models.BooleanField(default=True) #esto es necesario para el login. Aunque podemos ignorarlo en el modelo de datos. 
    is_active = models.BooleanField(default=True) #esto es necesario para el login. Aunque podemos ignorarlo en el modelo de datos.
    is_superuser = models.BooleanField(default=False) #esto es necesario para el login. Aunque podemos ignorarlo en el modelo de datos.

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['cc', 'fullname', 'phoneNumberU', 'password', 'birthday']

    def __str__(self):
            return self.fullname

    class Meta: 
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        

class CompanyManager(models.Manager): 
    def create_company(self, nit, name, phoneNumberC, address, user): 
            
        company = self.model(
            nit=nit, 
            name = name, 
            phoneNumberC = phoneNumberC, 
            address = address, 
            user = user, 
        )   
        return company


class Company(models.Model):
    nit = models.CharField(auto_created=False, primary_key=True, serialize=False, verbose_name='NIT', max_length=9)
    name = models.CharField(max_length=50)
    phoneNumberC = models.CharField(max_length=15)
    address = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = CompanyManager()
    
    REQUIRED_FIELDS = ['nit', 'name', 'phoneNumber', 'address', 'user']

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=30)
    objective = models.TextField()
    results = models.TextField()
    reach = models.TextField()
    state = models.TextField()
    ownerCompany = models.OneToOneField(Company, on_delete=models.CASCADE)
    photo= models.ImageField(null=True, blank=True, upload_to="images/")
    def __str__(self):
        return self.name + " by "+ self.ownerCompany.name

    
class Role(models.Model):
    rolName=models.CharField(max_length=20)
    def __str__(self):
        return self.rolName

class Roles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.fullname +"  "+self.role.rolName

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
    hour = models.TimeField(auto_now=False, auto_now_add=False)
    binnacle = models.ForeignKey(Binnacle, on_delete=models.CASCADE)
    def __str__(self):
        return self.state