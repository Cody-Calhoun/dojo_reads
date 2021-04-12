from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

# localhost:8000/create_user
def create_user(request):
    if request.method == "GET":
        return redirect("/")

    new_user = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = request.POST['password']
    )
    return redirect('/dashboard')
    # localhost:8000/dashboard

def dashboard(request):
    return render(request, 'dashboard.html')
