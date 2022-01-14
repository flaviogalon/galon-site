from django.shortcuts import get_object_or_404, render

from .models import Post


def home_page(request):
    # Django includes the slice on the resulting SQL query!!
    latests_posts = Post.objects.all().order_by('-date')[:3]

    return render(request, 'blog/index.html', {
        'posts': latests_posts
    })

def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, 'blog/all-posts.html', {
        'posts': all_posts
    })

def post_page(request, slug):
    post = get_object_or_404(Post, slug=slug)   # same as Post.objects.get(slug=slug)
    return render(request, 'blog/post-detail.html', {
        'post': post,
        'post_tags': post.tag.all()
    })
