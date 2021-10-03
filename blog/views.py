from django.shortcuts import render
from .models import Post
from django.views.generic import View


def index(request):
    allPosts= Post.objects.all()
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    context={
        'allPosts': allPosts,
        'object_list': featured,
        'latest': latest,
    }
    
    
    return render(request, "website/index.html", context)


def allblog(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, "website/allblog.html" , context)


def post(request, post):
    post = Post.objects.get(id=post)
    most_recent = Post.objects.order_by('-timestamp')[:5]

    
    context = {
        'post':post,
        'most_recent': most_recent,
    }
    
    context = {        
        'post':post,

    }
    return render(request, "website/post.html", context)


def contact(request):
    
    context = {}
    return render(request, "website/contact.html", context)