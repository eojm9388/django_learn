from rest_framework import serializers
from .models import Book

class BookTitleSerialize(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title',)
        
        
class BookSerialize(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'