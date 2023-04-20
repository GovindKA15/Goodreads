from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .data import books
from books.models import Book
from books.serializers import BookSerializer


class BookList(View):
    def get(self,request):
        return JsonResponse(books,safe=False)
class BookListById(View):
    def get(self,request,id): 
        book = next((book for book in books if book['id'] == id), None)
        return JsonResponse(book,safe=False)

