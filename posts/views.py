from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

@login_required
def create(request):
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
            return redirect("/")
    else:
        post_form = PostForm()
    context = {
        "post_form": post_form
    }
    return render(request, 'posts/create.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'posts/detail.html', context)

@login_required
def delete(request, post_id):
    if request.user == post.user:
        post = get_object_or_404(Post, id=post_id)
        post.delete()
    return redirect('/')

@login_required
def update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.user:
        if request.method=="POST":
            post_form = PostForm(request.POST, request.FILES, instance=post)
            if post_form.is_valid():
                post_form.save()
                return redirect("/")
        else:
            post_form = PostForm(instance=post)
    else:
        return redirect("posts:index")
    context = {
                'post_form': post_form,
            }
    return render(request, 'posts/update.html', context)

