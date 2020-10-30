## On line 2, you import the models you want to register on the admin page.
## On line 4 and line 7, you define empty classes PostAdmin and CategoryAdmin.
## The last two lines are the most important. These register the models with the admin classes.

from django.contrib import admin
from blog.models import Post, Category

class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)