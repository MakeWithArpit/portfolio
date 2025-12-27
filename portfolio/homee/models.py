from django.db import models

class description(models.Model):
    page_title = models.CharField(max_length=200)
    profile_photo = models.ImageField(upload_to='profile_photo/')
    short_description = models.CharField(max_length=130)
    long_Para1 = models.CharField(max_length=250)
    long_Para2 = models.CharField(max_length=250)
    long_Para3 = models.CharField(max_length=250)
    def __str__(self):
        return self.page_title

class social_links(models.Model):
    platform_name = models.CharField(max_length=100)
    link = models.URLField()
    link_with_username = models.CharField(max_length=100) # e.g., github.com/MakeWithArpit
    icon_class = models.CharField(max_length=100)
    def __str__(self):
        return self.platform_name

class work(models.Model):
    number_of_projects = models.IntegerField()
    number_of_certifications = models.IntegerField()
    started_year = models.IntegerField()

class qualifications(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    year = models.CharField(max_length=100)
    branch = models.CharField(max_length=200)
    def __str__(self):
        return self.degree

class skills(models.Model):
    skill_name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100)
    def __str__(self):
        return self.skill_name

class Certificates(models.Model):
    cert_title = models.CharField(max_length=200)
    cert_image = models.ImageField(upload_to='certificates/')
    issued_by = models.CharField(max_length=200)
    issue_date = models.CharField(max_length=100)

    def __str__(self):
        return self.cert_title

class Projects(models.Model):
    project_title = models.CharField(max_length=200)
    short_description = models.TextField()
    featured = models.BooleanField(default=False)
    technologies = models.TextField()
    points = models.TextField()

    def technologies_list(self):
        return [t.strip() for t in self.technologies.split("$")]

    def points_list(self):
        return [p.strip() for p in self.points.split("$")]

    def __str__(self):
        return self.project_title
