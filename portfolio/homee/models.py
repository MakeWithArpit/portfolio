from django.db import models

class description(models.Model):
    page_title = models.CharField(max_length=200)
    profile_photo = models.ImageField(upload_to='profile_photo/')
    short_description = models.TextField()
    long_Para1 = models.TextField()
    long_Para2 = models.TextField()
    long_Para3 = models.TextField()

class social_links(models.Model):
    platform_name = models.CharField(max_length=100)
    link = models.URLField()
    link_with_username = models.CharField(max_length=100) # e.g., github.com/MakeWithArpit
    icon_class = models.CharField(max_length=100)

class work(models.Model):
    number_of_projects = models.IntegerField()
    number_of_certifications = models.IntegerField()
    started_year = models.IntegerField()

class qualifications(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    year = models.CharField(max_length=100)
    branch = models.CharField(max_length=200)

class skills(models.Model):
    skill_name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100)

class Certificates(models.Model):
    cert_title = models.CharField(max_length=200)
    cert_image = models.ImageField(upload_to='certificates/')
    issued_by = models.CharField(max_length=200)
    issue_date = models.CharField(max_length=100)

class Projects(models.Model):
    project_title = models.CharField(max_length=200)
    short_description = models.TextField()
    featured = models.BooleanField(default=False)
    technologies = models.TextField()  # Comma-separated list of technologies
    points = models.TextField()  # Comma-separated list of points