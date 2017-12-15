# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

from .models import Author, Book


# Create your views here.

def index(request):

    return HttpResponse("<h1>BOOKS HOMEPAGE<h1>")

def book_details(request, book_id):
    books = Book.objects.all()
    book_id = int(book_id)

    books_content = Book.objects.all()[book_id]
    return HttpResponse("<h2>Book id %s.</h2> <br/>" \
                        "<b>Name:</b> %s</h2> <br/>" \
                        "<b>Author:</b> %s</h2> <br/>" \
                        "<b>Page Number:</b> %s</h2> <br/>" \
                        "<b>Publisher:</b> %s</h2> <br/>" \
                        "<b>Publish Date:</b> %s</h2> <br/>" \
                        "" % (str(book_id), books_content.book_name,  books_content.author, books_content.page_number,books_content.publisher,
                              books_content.publishdate))





