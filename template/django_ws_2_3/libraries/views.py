from django.shortcuts import render
import requests

API_KEY = '알라딘 api'
API_URL = f'http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey={API_KEY}&QueryType=ItemNewSpecial&MaxResults=50&start=1&SearchTarget=Book&output=js&Version=20131101'

# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
    response = requests.get(API_URL).json()
    book_list = []
    book_title = []
    book_author = []
    for book in response.get('item'):
        book_info = {}
        book_info['저자'] = book.get('author')
        book_author.append(book.get('author'))
        book_info['제목'] = book.get('title')
        book_title.append(book.get('title'))
        book_list.append(book_info)
    book_cnt = len(book_list)
    book_info = {}

    for i in range(book_cnt):
        book_info[book_title[i]] = book_author[i]
    context = {
        'book_info': book_info
    }

    return render(request, 'recommend.html', context)