from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken
from dimbaManager.apps.common.models import CommonFieldsMixin


class User(AbstractUser, CommonFieldsMixin):
    """ Base class for all users """
    class Types(models.TextChoices):
        NORMALUSER = "NORMALUSER", "NormalUser"
        FIELDMANAGER = "FIELDMANAGER", "FieldManager"
        CAPTAIN = "CAPTAIN", "Captain"
        STAFFMANAGER = "STAFFMANAGER", "StaffManager"
        ADMIN = "ADMIN", "Admin"

    base_type = Types.NORMALUSER
    type = models.CharField(
        verbose_name=_("Type"),
        max_length=50,
        choices=Types.choices,
        default=base_type
    )
    email = models.CharField(
        verbose_name=_("Email of User"),
        unique=True,
        max_length=255
    )


    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = self.base_type
        return super().save(*args, **kwargs)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        

""" ============================== Proxy Model Managers ========================== """
class NormalUserManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.NORMALUSER)
    
    def normalize_email(self, email):
        # Implement your email normalization logic here if needed
        return email.lower()
    

class AdminManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.ADMIN)
    
    def normalize_email(self, email):
        return email.lower()
    

class FieldManagerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.FIELDMANAGER)
    
    def normalize_email(self, email):
        return email.lower()


class CaptainManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.CAPTAIN)
    
    def normalize_email(self, email):
        return email.lower()
    

class StaffManagerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.STAFFMANAGER)
    
    def normalize_email(self, email):
        return email.lower()
    
""" =================== Proxy Models ================== """
class NormalUser(User):
    base_type = User.Types.NORMALUSER
    objects = NormalUserManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.NORMALUSER
            self.set_password(self.password)
        return super().save(*args, **kwargs)
    
    class Meta:
        proxy = True
        ordering = ['-created_at', '-updated_at']


class FieldManager(User):
    base_type = User.Types.FIELDMANAGER
    objects = FieldManagerManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.FIELDMANAGER
            self.set_password(self.password)
        return super().save(*args, **kwargs)
    
    class Meta:
        proxy = True
        ordering = ['-created_at', '-updated_at']


class Captain(User):
    base_type = User.Types.CAPTAIN
    objects = CaptainManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.CAPTAIN
            self.set_password(self.password)
        return super().save(*args, **kwargs)
    
    class Meta:
        proxy = True
        ordering = ['-created_at', '-updated_at']


class StaffManager(User):
    base_type = User.Types.STAFFMANAGER
    objects = StaffManagerManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.STAFFMANAGER
            self.set_password(self.password)
        return super().save(*args, **kwargs)
    
    class Meta:
        proxy = True
        ordering = ['-created_at', '-updated_at']


class Admin(User):
    base_type = User.Types.ADMIN
    objects = AdminManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.ADMIN
            self.set_password(self.password)
        return super().save(*args, **kwargs)
    
    class Meta:
        proxy = True
        ordering = ['-created_at', '-updated_at']
