from .models import *
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .forms import *
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect


def post(request):

    newpost = Post.objects.all().order_by("-created")[0:1]
    post = Post.objects.all().order_by("-created")[1:10]
    context={
        "newposts": newpost,
        "posts": post

    }

    return render(request, 'blog/blog.html', context)



class AddPost(CreateView):
    """ Добавление
    """
    model = Post
    form_class = PostForm
    template_name = "post_edit.html"
    success_url = reverse_lazy('posts')




