from django.shortcuts import render, redirect
from .form import LoginForm

# Create your views here.
def signin(request):
    login_form = LoginForm()
    return render(request, "login.html", locals())


def index(request):
    return render(request, "index.html")


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            login_username = request.POST['username'].strip()
            login_password = request.POST['password'].strip()
            if login_password == '123':
                return redirect('/index')
            else:
                message = "Login fail."
        else:
            message = "Please check username or password you input."
    else:
        login_form = LoginForm()

    return render(request, 'login.html', {"login_form": login_form})

