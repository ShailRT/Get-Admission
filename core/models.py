from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField()
    message = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
