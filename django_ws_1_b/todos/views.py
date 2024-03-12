from django.shortcuts import render

def index_view(request):
    return render(request, 'todos/index.html')
# Create your views here.
