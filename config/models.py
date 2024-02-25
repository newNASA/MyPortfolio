from django.db import models

# Create your models here.

class My_info(models.Model):
    fullname = models.CharField(max_length=75)
    img = models.ImageField(upload_to='imgs')
    title = models.CharField(max_length=200)
    job = models.CharField(max_length=100)
    info_title = models.CharField(max_length=250)
    birth_date = models.CharField(max_length=75)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    age = models.IntegerField()
    rank = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    info_text = models.TextField()

    def __str__(self) -> str:
        return "Men Haqimda"

class My_skills(models.Model):
    name= models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Interests(models.Model):
    img = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    

class My_social(models.Model):
    link = models.URLField(max_length=100)
    img = models.CharField(max_length=50)

    def __str__(self):
        return self.link

class My_projects(models.Model):
    CHOICES = (
        ('frontend', 'frontend'),
        ('backend', 'backend'),
    )
    img = models.ImageField(upload_to='imgs')
    name = models.CharField(max_length=50)
    category = models.CharField(choices=CHOICES, max_length=50)
    title = models.CharField(max_length=50)
    client = models.CharField(max_length=100)
    date = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.name