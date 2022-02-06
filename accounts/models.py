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
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    class Meta:
        verbose_name_plural = "CONTACT"



# Create your models here.
class About(models.Model):
    FREELANCE_CHOICES = (
        ("Available", "Available"),
        ("Not Available","Not Available")
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=200)
    profile = models.ImageField(upload_to="profile")
    cover = models.ImageField(upload_to="profile")
    website = models.URLField()
    dob = models.DateField()
    phone = models.CharField(max_length=10)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    freelance = models.CharField(max_length=200,choices=FREELANCE_CHOICES)
    age = models.CharField(max_length=10)
    degree = models.CharField(max_length=200)
    client = models.IntegerField()
    project = models.IntegerField()
    awards = models.IntegerField()
    support = models.IntegerField()
    description = models.TextField()

    class Meta:
        verbose_name_plural = "ABOUT"


# class Fact(models.Model):
#     type = models.ForeignKey(ConfigChoice, on_delete=models.CASCADE)
#     value = models.CharField(max_length=200)
#     logo = models.ImageField(upload_to="fact-logo")
#     description = models.TextField()
#
#     class Meta:
#         verbose_name_plural = "FACT"


class Skills(models.Model):
    type = models.ForeignKey(ConfigChoice, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)
    description = models.TextField(default="")

    class Meta:
        verbose_name_plural = "SKILLS"


class Testimonials(models.Model):
    name = models.CharField(max_length=200)
    post = models.CharField(max_length=250)
    profile = models.ImageField(upload_to="testimonials/")
    message = models.TextField()

    class Meta:
        verbose_name_plural = "TESTIMONIALS"


class Portfolio(models.Model):
    project_name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="portfolio/")
    category = models.ForeignKey(ConfigChoice, on_delete=models.CASCADE)
    client = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    url = models.URLField()
    description = models.TextField()


    class Meta:
        verbose_name_plural = "PORTFOLIO"


class Education(models.Model):
    degree = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    current_now = models.BooleanField()
    institute = models.CharField(max_length=250)
    marks = models.CharField(max_length=200)
    institute_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "EDUCATION"


class Experience(models.Model):
    job_title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current_working = models.BooleanField()
    company = models.CharField(max_length=250)
    company_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "EXPERIENCE"

#
# class Task(models.Model):
#     experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
#     task = models.TextField()
#
#     class Meta:
#         verbose_name_plural = "TASK"


class Services(models.Model):
    title = models.CharField(max_length=240)
    icon = models.ImageField(upload_to="services")
    description = models.TextField()


class Gallery(models.Model):
    project = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="gallery")

