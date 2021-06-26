from django.shortcuts import render, redirect
from django.http import HttpResponse

from . models import *

# Create your views here.

def blog(request):
    blog = Blog.objects.all().order_by('-date_created')
    context = {'blog' : blog}
    return render(request, 'blog.html', context)

def post(request, id):
    post = Blog.objects.get(id=id)
    context = {'post' : post}
    return render(request, 'post.html', context)