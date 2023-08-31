from django.db import models
from ckeditor.fields import RichTextField
from cms.models import College, Course

class Comment(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField()
    message = models.TextField(blank=True, null=True)
    college = models.ForeignKey(College, blank=True, null=True, on_delete=models.SET_NULL)
    course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email



