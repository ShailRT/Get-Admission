from django.db import models
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


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
    meta_description = models.TextField(blank=True, null=True)
    institute_type = models.CharField(max_length=120, choices=type_choices, default='college')
    slug = models.SlugField()
    image = models.ImageField(upload_to='header')
    logo = models.ImageField(upload_to='logo', blank=True, null=True)
    thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(416, 197)], format="PNG", options={'quality': 60})
    location = models.CharField(max_length=150)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    description = RichTextField()
    course_fees = RichTextField()
    placement = RichTextField()
    gallery = models.ManyToManyField(Gallery)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    star_count = models.PositiveIntegerField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    fee_range = models.CharField(max_length=120, blank=True, null=True)
    website = models.CharField(max_length=120, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=120)
    meta_description = models.TextField(blank=True, null=True)
    intro = models.CharField(max_length=220)
    slug = models.SlugField()
    image = models.ImageField(upload_to='header')
    description = RichTextField()
    course_fees = RichTextField()
    college = RichTextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title






