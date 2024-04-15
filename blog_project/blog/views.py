from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


posts = [
    {
        'author': 'Musa Mvuna',
        'title': 'First Blog',
        'content': 'My first ever blog content',
        'date_posted': 'May 4, 2024'
    },
    {
        'author': 'Jane Doe',
        'title': 'Second Blog',
        'content': 'My second blog content',
        'date_posted': 'May 5, 2024'
    },
    {
        'author': 'John Doe',
        'title': 'Third Blog',
        'content': 'My third blog content',
        'date_posted': 'May 6, 2024'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)
def about(request):
    return render(request, 'blog/about.html')