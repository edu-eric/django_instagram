from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        User.objects.create_user(username=username, password=password)
    return render(request, 'accounts/signup.html')