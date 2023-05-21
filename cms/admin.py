from django.contrib import admin
from .models import Gallery, Author, College

class CollegeAdmin(admin.ModelAdmin):
    search_fields = ['title', 'location']
    list_filter = ['institute_type']


admin.site.register(Gallery)
admin.site.register(Author)
admin.site.register(College, CollegeAdmin)
