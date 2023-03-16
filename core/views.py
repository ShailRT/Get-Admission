from django.shortcuts import render


def index(request):
    return render(request, 'static/home.html')

def about(request):
    return render(request, 'static/about.html')

def contact(request):
    return render(request, 'static/contact.html')