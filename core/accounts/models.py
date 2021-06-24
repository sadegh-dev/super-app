from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import MyUserManager


class User(AbstractBaseUser):
    email =         models.EmailField(max_length=254, unique=True)
    #password

    full_name =     models.CharField(max_length=200)
    national_code = models.CharField(max_length=10, unique=True ) #validate
    date_birth =    models.DateField() 
    
    mobile =        models.CharField(max_length=11, unique=True) #validate
    phone =         models.CharField(max_length=15, null=True, blank=True ) #validate 
    address =       models.TextField()
    
    ACCESS_LEVELS = (
        ('s','simple'),
        ('o','operator'),
        ('a','admin')
    )
    access_level =  models.CharField(max_lenght=1,  choices=ACCESS_LEVELS, default = 's')
    
    is_admin =      models.BooleanField(default=False)
    is_active =     models.BooleanField(default=True)
    
    created =       models.DateTimeField(auto_now_add=True)
    updated =       models.DateTimeField(auto_now=True)
    #book =         models.ForeignKey(Book, on_delete=models.SET_NULL) OR models.PositiveIntegerField(idBook or 0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'national_code', 'date_birth', 'mobile', 'address']
    objects = MyUserManager()

    def __str__(self):
        return f'{self.full_name} - {self.email} - {self.access_level}'

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_lable):
        return True

    @property
    def is_staff(self):
        return self.is_admin




