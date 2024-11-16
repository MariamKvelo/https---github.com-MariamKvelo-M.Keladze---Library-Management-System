from django.contrib import admin
from .models import Author, Genre, Book, BookIssue

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'quantity_in_stock')
    search_fields = ('title', 'authors__name', 'genre__name')
    list_filter = ('genre',)

class BookIssueAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'issue_date', 'return_date', 'is_returned')
    list_filter = ('is_returned', 'book')

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book, BookAdmin)
admin.site.register(BookIssue, BookIssueAdmin)
