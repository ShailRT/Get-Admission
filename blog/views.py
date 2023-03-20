from django.shortcuts import render

from .models import Blog
from core.forms import CommentForm

def blog_detail(request, pk):
    blog = Blog.objects.filter(slug=pk).first()
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'blog': blog,
        'form': form,
    }

    return render(request, 'blog-details.html', context)