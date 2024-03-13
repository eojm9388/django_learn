from django.shortcuts import render

# Create your views here.
def index(request):
    do_list = []
    do_list.append(request.GET.get('message')) 
    context = {
        'do_list': do_list
    }
    return render(request, 'todos/index.html', context)

def create_todo(request):
    return render(request, 'todos/create_todo.html')