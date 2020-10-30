from django.db import models
# Create your models here. This is where we represent database tables that are refereed to as a model, We created a class name model
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()   # Text field similar to charfield but it doesnt have maximum length limit 
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")  # This holds a string but must point to a file path name

