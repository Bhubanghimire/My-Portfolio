from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Address, ConfigChoice
User = get_user_model()


# Create your models here.
class About(models.Model):
    FREELANCE_CHOICES = (
        ("Avaiable", "Avaiable"),
        ("Not Avaiable","Not Avaiable")
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    website = models.URLField()
    bod = models.DateField()
    phone = models.CharField(max_length=10)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    freelance = models.CharField(max_length=200,choices=FREELANCE_CHOICES)
    age = models.CharField(max_length=10)
    degree = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "ABOUT"


class Fact(models.Model):
    type = models.ForeignKey(ConfigChoice, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="fact-logo")
    description = models.TextField()

    class Meta:
        verbose_name_plural = "FACT"


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
    type = models.ForeignKey(ConfigChoice,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "PORTFOLIO"


class Education(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    current_now = models.CharField(max_length=10)
    institute = models.CharField(max_length=250)
    marks = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "EDUCATION"


class Experience(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "EXPERIENCE"


class Task(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    task = models.TextField()

    class Meta:
        verbose_name_plural = "TASK"



