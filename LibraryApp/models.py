from django.db import models


class Accounts(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    accType = models.CharField(max_length=100)


class Book(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    ISBN = models.CharField(max_length=20)
    author = models.CharField(max_length=100)
    borrow_user = models.CharField(max_length=300, null=True)
    publication_year = models.IntegerField(null=True)
