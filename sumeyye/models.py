# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.

class Author (models.Model):
    name = models.CharField(max_length=30)
    author_country = models.CharField(max_length=30)
    author_language = models.CharField(max_length=30)

    def __str__(self):
        return self.name + " - " + self.author_country


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=50)
    page_number = models.CharField(max_length=5)
    publisher = models.CharField(max_length=100)
    publish_date= models.CharField(max_length=5)

    def __str__(self):
        return self.book_name



