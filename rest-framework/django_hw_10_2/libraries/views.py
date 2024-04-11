from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import BookTitleSerialize, BookSerialize

from .models import Book

# Create your views here.

@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookTitleSerialize(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def book_detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    serializer = BookSerialize(book)
    
    return Response(serializer.data)