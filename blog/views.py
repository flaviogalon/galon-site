from django.shortcuts import render

def home_page(request):
    return render(request, 'blog/index.html')

def posts(request):
    return render(request, 'blog/all-posts.html')

def post_page(request, slug):
    return render(request, 'blog/post-detail.html')