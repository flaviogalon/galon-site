from django.shortcuts import render

def home_page(request):
    return render(request, 'blog/index.html')

def posts(request):
    pass

def post_page(request):
    pass