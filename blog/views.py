from django.shortcuts import render
from datetime import date

dummy_posts = [
    {
        'slug': 'first-post',
        'image': 'django.png',
        'author': 'Galon',
        'date': date(2021, 11, 4),
        'title': 'Learning Django',
        'excerpt': 'Well, writting a blog in Django sounds like an overkill.',
        'content': '''
            Lorem ipsum dolor sit amet consectetur adipisicing elit.
            Non natus asperiores laborum consequuntur esse ipsa vel architecto
            nihil accusantium sapiente aperiam, aliquam, alias facilis ducimus
            culpa ipsum, soluta dolores eligendi.
        '''
    },
    {
        'slug': 'second-post',
        'image': 'voldemort.jpg',
        'author': 'Galon',
        'date': date(2021, 12, 6),
        'title': 'Voldemort',
        'excerpt': 'Voldemort seems like a cool guy',
        'content': '''
            Lorem ipsum dolor sit amet consectetur adipisicing elit.
            Non natus asperiores laborum consequuntur esse ipsa vel architecto
            nihil accusantium sapiente aperiam, aliquam, alias facilis ducimus
            culpa ipsum, soluta dolores eligendi.
        '''
    },
    {
        'slug': 'third-post',
        'image': 'rooster.jpg',
        'author': 'Galon',
        'date': date(2021, 11, 5),
        'title': 'A rooster',
        'excerpt': 'I like roosters',
        'content': '''
            Lorem ipsum dolor sit amet consectetur adipisicing elit.
            Non natus asperiores laborum consequuntur esse ipsa vel architecto
            nihil accusantium sapiente aperiam, aliquam, alias facilis ducimus
            culpa ipsum, soluta dolores eligendi.
        '''
    },
]

def home_page(request):
    sorted_posts = sorted(dummy_posts, key=lambda post: post['date'])
    latest_posts = sorted_posts[-3:]

    return render(request, 'blog/index.html', {
        'posts': latest_posts
    })

def posts(request):
    return render(request, 'blog/all-posts.html', {
        'posts': dummy_posts
    })

def post_page(request, slug):
    post = next(post for post in dummy_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {
        'post': post
    })