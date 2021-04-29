from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class UserProfileManager(BaseUserManager):
    """Custom manager for Custom user model"""

    def create_user(self, email, name, password=None):
        """create a new user profile"""

        if not email:
            raise ValueError('User must have a email ID')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """create super user"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""

    name = models.CharField(max_length=64)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(max_length=255, unique=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """"Retrieve user full name"""

        return self.name

    def get_short_name(self):
        """Retrieve user short name"""

        return self.name

    def __str__(self):
        """String repr of user model"""

        return f'{self.email} : {self.name}'




