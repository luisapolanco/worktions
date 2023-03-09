from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self, username, email, name, id, city, is_staff, is_superuser, password=None):
        user = self.model(
            username=username,
            email=email,
            name=name,
            id= id,
            city = city,
            is_staff=is_staff,
            is_superuser=is_superuser,            
        )
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, email, name, id, city, is_staff, password):
        return self._create_user(username, email, name, id, city, is_staff, False, password)
    
    def create_superuser(self,username,email,name,  id, city, password):
        return self._create_user(username, email, name, id, city, True, True, password)

class User(AbstractBaseUser):
    username = models.CharField('Nombre de usuario',unique = True, max_length=100)
    email = models.EmailField('Correo Electrónico', max_length=254,unique = True)
    name = models.CharField('Nombres', max_length=200, blank = True, null = True)    
    id = models.CharField(max_length=15, primary_key=True)
    date_of_birth = models.DateField()
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length =20)
    phone = models.CharField(max_length =15)
    gender = models.CharField(max_length=15)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name','email', 'id', 'city']

    def __str__(self) -> str:
        return f'{self.id}, {self.name}'
    
    def has_perm(self, perm, obj= None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property    
    def is_staff(self):
        return self.is_staff
    

class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=25)
    def __str__(self) -> str:
        return '{}'.format(self.name)

class Service(models.Model):
    id = models.BigAutoField(primary_key=True)
    title= models.CharField(max_length= 50, default='')
    user_id = models.ForeignKey(User, null= False, blank=False, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, null= False, blank=False, on_delete=models.CASCADE)
    description = models.CharField(max_length = 250, default='')
    images = models.ImageField(upload_to="services/images", null=True)
