from django.contrib import admin

# Register your models here.
from .models import Publisher, Book, Review

admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Review)