from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [

    {
        'author': 'Mike Tyson',
        'title': 'post me',
        'content': 'first post',
        'date_posted': 'january 2nd 2022'
    },
    {
        'author': 'Huy Chau',
        'title': 'post me',
        'content': 'second post',
        'date_posted': 'march 12, 2022'
    }

]


def home(request):
    context = {
        'posts': posts 
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
