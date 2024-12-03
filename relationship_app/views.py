# relationship_app/views.py
from django.shortcuts import render
from .models import Book, Library, Librarian, Author
from django.views.generic import DetailView

def list_books(request):
    # الحصول على جميع الكتب من قاعدة البيانات
    books = Book.objects.all()
    # تمرير الكتب إلى القالب
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetail(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
