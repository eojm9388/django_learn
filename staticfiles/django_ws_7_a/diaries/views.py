from django.shortcuts import render, redirect
from .models import Diray
from .forms import DiaryForm

# Create your views here.
def index(request):
    diaries = Diray.objects.all()
    context = {
        'diaries': diaries
    }

    return render(request, 'diaries/index.html', context)

def create(request):
    if request.method == "POST":
        form = DiaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diaries:index')
    else:
        form = DiaryForm()

    context = {
        'form': form,
    }
    
    return render(request, 'diaries/create.html', context)