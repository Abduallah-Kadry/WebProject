from django.contrib import admin

from .models import *


admin.site.register(Book)
admin.site.register(Accounts)
admin.site.register(BorrowList)

# Register your models here.
