from django.shortcuts import render

from .models import Book


# Create your views here.

def home(request):
    return render(request, 'LibraryApp/home.html')


def register(request):
    return render(request, 'LibraryApp/registration.html')


def login(request):
    return render(request, 'LibraryApp/login.html')


def librarian(request):
    return render(request, 'LibraryApp/librarian.html')


def user(request):
    books = Book.objects.all()

    return render(request, 'LibraryApp/user.html', {'book_list': books})


def feedback(request):
    return render(request, 'LibraryApp/feedback.html')
