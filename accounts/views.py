from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('/')
    else:
        user_form = UserCreationForm()
    context = {
        'user_form': user_form,
    }
    return render(request, 'accounts/signup.html', context)