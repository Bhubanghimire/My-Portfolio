from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from system.models import ConfigChoice


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an Email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password=password, **extra_fields)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    CHOICES = (
        ('MALE', 'Male'),
        ('Female', 'Female'),
    )
    email = models.EmailField(max_length=255, unique=True, verbose_name="Email Address")
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, choices=CHOICES)
    profile_img = models.ImageField(upload_to="profile", null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


    class Meta:
        verbose_name_plural = "USER"


User = get_user_model()


class Address(models.Model):
    type = models.ForeignKey(ConfigChoice, on_delete=models.CASCADE)
    country = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "ADDRESS"


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    class Meta:
        verbose_name_plural = "CONTACT"