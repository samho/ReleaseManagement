from django.shortcuts import render, redirect
from .form import LoginForm
from utils import dbmanager

# Create your views here.
def signin(request):
    login_form = LoginForm()
    return render(request, "login.html", locals())


def index(request):
    return render(request, "index.html")


def login(request):
    message = ""
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            login_username = request.POST['username'].strip()
            login_password = request.POST['password'].strip()
            submit_user = dbmanager.find_user_by_username(login_username)
            if submit_user is not None:
                if submit_user.verify_password(login_password):
                    return redirect('/index')
                else:
                    message = "User Name or Password is not correct."
            else:
                message = "User not found."
        else:
            message = "Please check username or password you input."
    else:
        login_form = LoginForm()

    if message == "":
        return render(request, 'login.html', {"login_form": login_form})
    else:
        return render(request, 'login.html', {"login_form": login_form, "message": message})


