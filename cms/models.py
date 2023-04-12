from django.db import models
from ckeditor.fields import RichTextField


type_choices =(
    ('University', 'university'),
    ('College', 'college')
)

class Gallery(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.title 

class Author(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='author')

    def __str__(self):
        return self.name

class College(models.Model):
    title = models.CharField(max_length=120)
    institute_type = models.CharField(max_length=120, choices=type_choices, default='college')
    slug = models.SlugField()
    image = models.ImageField(upload_to='header')
    location = models.CharField(max_length=150)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    description = RichTextField()
    gallery = models.ManyToManyField(Gallery)
    rating = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title





