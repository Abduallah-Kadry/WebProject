from django.contrib import admin

from .models import Book
from .models import Accounts

admin.site.register(Book)
admin.site.register(Accounts)

# Register your models here.
