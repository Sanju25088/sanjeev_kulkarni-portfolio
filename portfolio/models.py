from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    USER_TYPE = [('admin','Admin')]

    user_type = models.CharField(max_length=20,default='admin')
    profile_image = models.ImageField(upload_to='profile_image/',blank=True,null=True)

class Personal_Information(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100, null = True,blank = True)
    designation = models.CharField(max_length=100,null = True,blank = True)
    tagline = models.CharField(max_length=100, null = True,blank = True)
    about = models.TextField(blank = True,null =True)
    phone =	models.CharField(max_length=10,null =True,blank = True)
    email =	models.EmailField(unique = True,null =True,blank = True)
    address	= models.CharField(max_length=100,null =True,blank = True)
    city = 	models.CharField(max_length=50,null =True,blank = True)
    state = models.CharField(max_length=50,null =True,blank = True)
    country	= models.CharField(max_length=50,null =True,blank = True)
    github = models.URLField(max_length=200,null =True,blank = True)
    linkedin = models.URLField(max_length=200,null =True,blank = True)
    portfolio_url =	models.URLField(max_length=200,null =True,blank = True)
    resume = models.FileField(upload_to='resumes/',blank = True,null=True)
    profile_photo = models.ImageField(upload_to='profile_image/',blank=True,null = True)

class Education(models.Model):
    id = models.AutoField(primary_key=True)
    level = models.CharField(max_length=20, null = True,blank = True)
    stream_or_course = models.CharField(max_length=20,null = True,blank = True)
    institution = models.CharField(max_length=100,null = True,blank = True)
    location = models.CharField(max_length=50,null = True,blank = True)
    score_type = models.CharField(max_length=20,null = True,blank = True)
    score_value = models.FloatField(max_length=10,null = True,blank = True)
    start_year = models.DateField(blank=True,null = True)
    end_year = models.DateField(blank=True,null = True)
    edu_image = models.ImageField(upload_to='edu_image/',blank=True,null = True)



class Technical_Skils(models.Model):
    CATEGORY_CHOICES = [
        ('Web Frameworks', 'Web Frameworks'),
        ('Libraries','Libraries'),
        ('Frontend', 'Frontend'),
        ('Languages', 'Languages'),
        ('Database', 'Database'),
        ('Tools', 'Tools'),
    ]
     
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES,null=True,blank = True)
    skill_name = models.CharField(max_length=50,null=True,blank = True)
    skill_image = models.ImageField(upload_to='skill_image/',blank=True,null = True)
    proficiency = models.IntegerField(default=0, help_text='Skill proficiency percentage (0-100)')

class Internship(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.CharField(max_length=200,null=True,blank = True)
    role = models.CharField(max_length=50,null=True,blank = True)
    start_year = models.DateField(blank=True,null = True)
    end_year = models.DateField(blank=True,null = True)
    internship_image = models.ImageField(upload_to='internship_image/',blank=True,null = True)


class Key_Projects(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200,null=True,blank = True)
    description	= models.TextField(blank = True,null = True)
    technologies = 	models.TextField(blank = True,null = True)
    domain = models.CharField(max_length=50,null=True,blank = True)
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE, related_name="projects", blank =True,null=True)
    project_image = models.CharField(max_length=255,blank=True,null = True)
    project_link = models.URLField(max_length=200,null =True,blank = True)

class Certifications(models.Model):
    id = models.AutoField(primary_key=True)
    organization = models.CharField(max_length=200,null=True,blank = True)
    title = models.CharField(max_length=200,null=True,blank = True)
    location = models.CharField(max_length=200,null=True,blank = True)
    year = models.DateField(blank=True,null = True)

class Extracurricular_Activities(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=50,null=True,blank = True)
    organization = models.CharField(max_length=200,null=True,blank = True)
    event_name = models.CharField(max_length=200,null=True,blank = True)
    description = models.TextField(null=True,blank = True)
    year = models.DateField(null=True,blank = True)


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,null=True,blank = True)
    email = models.EmailField(null=True,blank = True)
    message = models.TextField(null=True,blank = True)
    created_at = models.DateTimeField(auto_now_add=True)  



