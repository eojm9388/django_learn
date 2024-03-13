import requests
from pprint import pprint

API_KEY = '알라딘 api'
API_URL = f'http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey={API_KEY}&QueryType=ItemNewSpecial&MaxResults=50&start=1&SearchTarget=Book&output=js&Version=20131101'

response = requests.get(API_URL).json()

book_list = []
for book in response.get('item'):
    book_info = {}
    book_info['국제 표준 도서 번호'] = book.get('isbn')
    book_info['저자'] = book.get('author')
    book_info['제목'] = book.get('title')
    book_info['출간일'] = book.get('pubdate')

    book_list.append(book_info)

pprint(book_list)
# pprint(response)
# print(response)