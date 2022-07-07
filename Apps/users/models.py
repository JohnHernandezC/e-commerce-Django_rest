from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin       
from django.contrib.contenttypes.models import ContentType
from django.forms import ValidationError 
from simple_history.models import HistoricalRecords    



class UserManager(BaseUserManager):
    def _create_user(self, username, email, nombres, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username=username,
            email=email,
            nombres=nombres,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, nombres, is_staff, password=None, **extra_fields):
        return self._create_user(username, email, nombres, password, is_staff, False, **extra_fields)
    
    def create_superuser(self,username,email,nombres,password = None,**extra_fields):
        return self._create_user(username, email, nombres, password, True, True, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin ):
    username = models.CharField('Nombre de usuario',unique = True, max_length=100)
    email = models.EmailField('Correo Electrónico', max_length=254,unique = True)
    nombres = models.CharField('Nombres', max_length=200)
    apellidos = models.CharField('Apellidos', max_length=200,blank = True, null = True)
    imagen = models.ImageField('Imagen de Perfil', max_length=200,blank = True,null = True)
    is_active = models.BooleanField(default = True)
    is_staff  = models.BooleanField(default = False)
    historical=HistoricalRecords()
    objects = UserManager()

    USERNAME_FIELD='username' #hace referencia al parametro unico puede ser esto o el coreo
    REQUIRED_FIELDS=['email','nombres','apellidos']#campos requeridos al momento de crear por consola
    
    
    def __str__(self):
        return self.nombres
   
            
     