from django.shortcuts import render
# Create your views here.

def index_website(request):
	context = locals()
	template = 'index_website.html'
	return render(request, template, context)
