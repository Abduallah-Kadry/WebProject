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
        emailtemp = request.POST.get('email')
        passTemp = request.POST.get('password')
        if emailtemp == Accounts.objects.get(email=emailtemp) & passTemp == Accounts.objects.get(password=passTemp):
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


def add_book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('Description')
        ISBN = request.POST.get('ISBN')
        author = request.POST.get('author')
        publication_year = request.POST.get('publication_year')

        book = Book(name=name, desc=description, ISBN=ISBN, author=author, publication_year=publication_year)
        book.save()

    return render(request, 'LibraryApp/addBook.html')


def book_details(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'LibraryApp/bookDetails.html', {'book': book})


def book_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'LibraryApp/delete.html', {'book': book})


def book_edit(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'LibraryApp/editBook.html', {'book': book})


def book_borrow(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'LibraryApp/borrow.html', {'book': book})
