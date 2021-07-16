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
        try:
            Accounts.objects.get(email=email)
            return redirect('error_email_already_exist')  # already exist error for email register
        except Accounts.DoesNotExist:
            pass

        password = request.POST.get('password1')

        phone = request.POST.get('phone')
        try:
            Accounts.objects.get(phone=phone)
            return redirect('error_phone_already_exist')  # already exist error for phone register
        except Accounts.DoesNotExist:
            pass

        if request.POST.get('radbtn') == 'userRadio':
            acctype = 'User'
        else:
            acctype = 'Librarian'

        account = Accounts(name=name, email=email, password=password, accType=acctype, phone=phone)
        account.save()
        return redirect('register_successful')

    return render(request, 'LibraryApp/registration.html')


def login(request):
    if request.method == 'POST':
        try:
            account_email = Accounts.objects.get(email=request.POST.get('email'))
        except Accounts.DoesNotExist:
            return redirect('error_email_does_not_exist')  # email doesn't exist error for login
        try:
            account_password = Accounts.objects.get(password=request.POST.get('password'))
        except Accounts.DoesNotExist:
            return redirect('error_wrong_password')  # wrong password error for login
        except Accounts.MultipleObjectsReturned:
            pass

        return login_successful(request, account_email)

    return render(request, 'LibraryApp/login.html')


def librarian(request, account_id):
    books = Book.objects.all()
    account = Accounts.objects.get(id=account_id)

    return render(request, 'LibraryApp/librarian.html', {'book_list': books, 'account': account})


def user(request, account_id):
    books = Book.objects.all()
    account = Accounts.objects.get(id=account_id)

    return render(request, 'LibraryApp/user.html', {'book_list': books, 'account': account})


def feedback(request):
    return render(request, 'LibraryApp/feedback.html')


def add_book(request, account_id):
    account = Accounts.objects.get(id=account_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('Description')
        ISBN = request.POST.get('ISBN')
        author = request.POST.get('author')
        publication_year = request.POST.get('publication_year')

        book = Book(name=name, description=description, ISBN=ISBN, author=author, publication_year=publication_year)
        book.save()
        return redirect('add_book_successful', account_id)

    return render(request, 'LibraryApp/addBook.html', {'account': account})


def book_details(request, book_id, account_id):
    book = Book.objects.get(id=book_id)
    account = Accounts.objects.get(id=account_id)
    return render(request, 'LibraryApp/bookDetails.html', {'book': book, 'account': account})


def book_delete(request, book_id, account_id):
    book = Book.objects.get(id=book_id)
    account = Accounts.objects.get(id=account_id)
    if request.method == 'POST':
        book.delete()
        return redirect('librarian', account_id)

    return render(request, 'LibraryApp/delete.html', {'book': book, 'account': account})


def book_edit(request, book_id, account_id):
    book = Book.objects.get(id=book_id)
    account = Accounts.objects.get(id=account_id)
    if request.method == 'POST':
        book.name = request.POST.get('name')
        book.description = request.POST.get('Description')
        book.ISBN = request.POST.get('ISBN')
        book.author = request.POST.get('author')
        book.publication_year = request.POST.get('publication_year')
        book.save()

    return render(request, 'LibraryApp/editBook.html', {'book': book, 'account': account})


def book_borrow(request, book_id, account_id):
    account = Accounts.objects.get(id=account_id)
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.borrow_user = "borrowed to user no." + str(account_id)
        book.save()
        return redirect('borrow_successful', account_id)

    return render(request, 'LibraryApp/borrow.html', {'book': book, 'account': account})


def cancel_borrow(request, book_id, account_id):
    account = Accounts.objects.get(id=account_id)
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.borrow_user = None
        book.save()
        return redirect('bookDetails', book_id, account_id)
    return render(request, 'LibraryApp/cancel_borrow.html', {'account': account, 'book': book})


def borrow_successful(request, account_id):
    account = Accounts.objects.get(id=account_id)
    return render(request, 'LibraryApp/borrow_successful.html', {'account': account})


def register_successful(request):
    return render(request, 'LibraryApp/register_successful.html')


def login_successful(request, context):
    return render(request, 'LibraryApp/Login_Successful.html', {'context': context})


def add_book_successful(request, account_id):
    account = Accounts.objects.get(id=account_id)
    return render(request, 'LibraryApp/bookAdd_Successful.html', {'account': account})


def error_email_already_exist(request):
    return render(request, 'LibraryApp/errorEmailAlreadyExist.html')


def error_email_does_not_exist(request):
    return render(request, 'LibraryApp/error_email_does_not_exist.html')


def error_wrong_password(request):
    return render(request, 'LibraryApp/error_wrong_password.html')


def error_phone_already_exist(request):
    return render(request, 'LibraryApp/errorPhoneAlreadyExist.html')
