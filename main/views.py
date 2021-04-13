from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'index.html')

# localhost:8000/user/create_user
def create_user(request):
    if request.method == "POST":
        # Validation check before DB save
        errors = User.objects.registration_validator(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request, value)
            return redirect('/')
        # print(request.POST['password'])

        hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        # print(hash_pw)
        new_user = User.objects.create(
            name = request.POST['name'],
            alias = request.POST['alias'],
            email = request.POST['email'],
            password = hash_pw
        )
        request.session['logged_user'] = new_user.id

        return redirect('/user/dashboard')
    return redirect("/")
    # localhost:8000/dashboard

def login(request):
    if request.method == "POST":
        user = User.objects.filter(email = request.POST['email'])

        if user:
            log_user = user[0]

            if bcrypt.checkpw(request.POST['password'].encode(), log_user.password.encode()):
                request.session['logged_user'] = log_user.id
                return redirect('/user/dashboard')
            messages.error(request, "Email or password are incorrect.")
            
    return redirect("/")


def dashboard(request):

    context = {
        'logged_user' : User.objects.get(id=request.session['logged_user'])
    }
    return render(request, 'dashboard.html', context)
