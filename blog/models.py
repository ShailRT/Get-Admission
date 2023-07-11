from django.db import models

from ckeditor.fields import RichTextField 

from cms.models import Author

class Blog(models.Model):
    title = models.CharField(max_length=120)
    meta_description = models.TextField(blank=True, null=True)
    intro = models.TextField(blank=True, null=True)
    slug = models.SlugField()
    image = models.ImageField(upload_to='blog')
    category = models.TextField()
    tags = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    body = RichTextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']    
        
    def __str__(self):
        return self.title 
    
    
