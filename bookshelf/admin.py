from django.contrib import admin
from .models import Book


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author','publication_year']
    list_filter = ['author', 'publication_year']
    search_fields = ['title', 'author']
    list_editable = ['publication_year']
    


admin.site.register(Book, BookAdmin)
admin.site.site_header = 'ALX'
admin.site.site_title = 'ALX'