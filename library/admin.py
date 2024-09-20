from django.contrib import admin
from .models import Book, Author, Category

# Register your models here.
@admin.register(Book)
class BOokAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'publication_date']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
