from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Posts

# Create your views here.
def home(request):
   # return HttpResponse('Hello from posts')

    #create a post object from the model  to  loop thru all the #posts available ie up to 10
    
    posts = Posts.objects.all()[:10]
    
    context = {
        'title': 'Latest posts',
        'posts': posts
    }

    return render(request, 'posts/index.html', context)
def details(request, id):
    try:
        post = Posts.objects.get(id=id)
    except Posts.DoesNotExist:
        raise Http404("Post Doesnt exist")
    
    context = {
        'post': post
    }

    return render(request, 'posts/details.html', context)