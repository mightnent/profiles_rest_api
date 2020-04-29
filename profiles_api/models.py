from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    """override the BaseUserManager"""
    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError("Users must have email address")
        #normalize just makes the second half of email all lower case
        email = self.normalize_email(email)
        user = self.model(email = email,name = name)

        #password is hashed
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self,email,name,password):
        user = self.create_user(email,name,password)
        #is_superuser is auto created by PermissionsMixin class
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """database model for users in the system"""
    email = models.EmailField(max_length=254, unique = True)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    UPM = UserProfileManager()

    #cuz we overridding
    USERNAME_FIELD = 'email' #this is default to required
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email