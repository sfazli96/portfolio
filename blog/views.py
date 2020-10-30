## blog_index will display a list of all your posts.
## blog_detail will display the full post as well as comments and a form to allow users to create new comments.
## blog_category will be similar to blog_index, but the posts viewed will only be of a specific category chosen by the user.
## On line 2, you import the Post and the Comment models, and on line 5 inside the view function, 
## you obtain a Queryset containing all the posts in the database. order_by() orders the Queryset according to the argument given
## On line 34, we create an instance of our form class. Don’t forget to import your form at the beginning of the file:

from django.shortcuts import render
from blog.models import Post, Comment 
from .forms import CommentForm 

def blog_index(request):
	posts = Post.objects.all().order_by('-created-on')
	context = {
		"posts": posts,
	}
	return render(request, "blog_index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(             ## you’ve used a Django Queryset filter. The argument of the filter tells Django what conditions need to be met for an object to be retrieved.
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)       ## The view function takes a pk value as an argument and this line retrieves the object with the given pk.

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)   ## Now, we retrieve all the comments assigned to the given post using Django filters again
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, "blog_detail.html", context)