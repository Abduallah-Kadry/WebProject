"""WebProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from LibraryApp import views
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home' ),
    path('register/',views.register,name='register' ),
    path('login/',views.login,name='login' ),
    path('student/<int:account_id>',views.student,name='student' ),
    path('Admin/<int:account_id>',views.Admin,name='Admin' ),
    path('feedback/',views.feedback,name='feedback' ),

    path('addBook/<int:account_id>',views.add_book,name='addBook' ),
    path('bookDetails/<int:book_id>/<int:account_id>',views.book_details,name='bookDetails' ),
    path('delete/<int:book_id>/<int:account_id>',views.book_delete,name='deleteBook' ),
    path('edit/<int:book_id>/<int:account_id>',views.book_edit,name='editBook' ),
    path('borrow/<int:book_id>/<int:account_id>',views.book_borrow,name='borrowBook' ),
    path('borrow_list/<int:account_id>',views.borrow_book_list,name='borrow_list' ),
    path('borrow_detail/<int:borrow_id>/<int:account_id>',views.borrow_detail,name='borrow_detail' ),

    path('login_successful/',views.login_successful,name='login_successful' ),
    path('register_successful/',views.register_successful,name='register_successful' ),

    path('borrow_request_accepted/<int:borrower_id>',views.borrow_request_accepted,name='borrow_request_accepted' ),
    path('borrow_request_refused/<int:borrower_id>',views.borrow_request_refused,name='borrow_request_refused' ),
    path('cancelBorrow/<int:book_id>/<int:account_id>',views.cancel_borrow,name='cancelBorrow' ),

    path('add_book_successful/<int:account_id>',views.add_book_successful,name='add_book_successful' ),
    path('borrow_request_successful/<int:account_id>',views.borrow_request_successful,name='borrow_request_successful' ),
    path('edit_book_successful/<int:account_id>',views.edit_book_successful,name='edit_book_successful' ),


    path('errorEmailAlreadyExist/',views.error_email_already_exist,name='error_email_already_exist' ),
    path('errorEmailDoesnotExist/',views.error_email_does_not_exist,name='error_email_does_not_exist' ),
    path('errorWrongPassword/',views.error_wrong_password,name='error_wrong_password' ),
    path('errorPhoneAlreadyExist/',views.error_phone_already_exist,name='error_phone_already_exist' ),


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
