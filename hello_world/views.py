from django.shortcuts import render

def hello_world(request):     # Takes in one argument. This object is an httpRequestObject that is created when a page is loaded. It contaitns information about reques, such as values like GET and POST
	return render(request, 'hello_world.html', {})  # Will render HTML file hello world
 
# Create your views here.
