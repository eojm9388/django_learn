from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def dtl_practice(request):
    lunch = ['밥', '국', '반찬', '음료수']
    empty = []
    context = {
        'lunch': lunch,
        'empty': empty,
    }
    return render(request, 'articles/dtl_practice.html', context)


def profile(request, username):
    context = {
        'username': username
    }

    return render(request, 'articles/profile.html', context)