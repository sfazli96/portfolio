## On line 9, the DateTimeField takes an argument auto_now_add=True. This assigns the current date and time to this field whenever an instance of this class is created.
## On line 10, the DateTimeField takes an argument auto_now=True. This assigns the current date and time to this field whenever an instance of this class is saved. 
## That means whenever you edit an instance of this class, the date_modified is updated.
## On line 20, we use another relational field, the ForeignKey field. This is similar to the ManyToManyField but instead defines a many to one relationship. 
## The reasoning behind this is that many comments can be assigned to one post. But you can’t have a comment that corresponds to many posts.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
