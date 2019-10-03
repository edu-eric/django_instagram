from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

def create(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect("/")
    else:
        post_form = PostForm()
    context = {
        "post_form": post_form
    }
    return render(request, 'posts/create.html', context)