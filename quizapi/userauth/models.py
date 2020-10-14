from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.shortcuts import reverse


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        if not password:
            raise ValueError('Users must have an email password')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    active      = models.BooleanField(default=False)
    staff       = models.BooleanField(default=False)
    admin       = models.BooleanField(default=False)
    teacher     = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):          
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    @property
    def is_teacher(self):
        return self.teacher
    
class UserProfile(models.Model):

    user        = models.OneToOneField(User, on_delete=models.CASCADE, related_name ='profile')
    name        = models.CharField(max_length = 30) 
    course      = models.CharField(max_length = 50, blank=True, null=True)
    branch      = models.CharField(max_length = 50, blank=True, null=True)
    section     = models.CharField(max_length = 50, blank=True, null=True)
    picture     = models.ImageField(upload_to = 'pictures/', blank = True, null = True, max_length = 1000)

    def __str__(self):
        return self.name