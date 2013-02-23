from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

class Issue(models.Model):
    issue = models.ForeignKey(Project)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')
    
class Field(models.Model):
    issue = models.ForeignKey(Issue)
    name = models.CharField(max_length=200)
    
