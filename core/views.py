from django.shortcuts import render
from .forms import CommentForm



def index(request):
    return render(request, 'static/home.html')

def about(request):
    return render(request, 'static/about.html')

def contact(request):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form,
    }
    return render(request, 'static/contact.html', context)

