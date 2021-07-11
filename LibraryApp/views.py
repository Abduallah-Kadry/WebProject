from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .models import *


# Create your views here.

def home(request):
    return render(request, 'LibraryApp/home.html')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        phone = request.POST.get('phone')
        if request.POST.get('radbtn') == 'userRadio':
            acctype = 'user'
        else:
            acctype = 'librarian'   

        account = Accounts(name=name, email=email, password=password, accType=acctype, phone=phone)
        account.save()

    return render(request, 'LibraryApp/registration.html')


def login(request):
    if request.method == 'POST':
        if request.POST.get('email') == Accounts.objects.get('email') & request.POST.get(
                'password') == Accounts.objects.get('password',):
            if Accounts.objects.get('accType') == 'user':
                return redirect('user.html')
            else:
                return redirect('librarian.html')

    return render(request, 'LibraryApp/login.html')


def librarian(request):
    return render(request, 'LibraryApp/librarian.html')


def user(request):
    books = Book.objects.all()

    return render(request, 'LibraryApp/user.html', {'book_list': books})


def feedback(request):
    return render(request, 'LibraryApp/feedback.html')
