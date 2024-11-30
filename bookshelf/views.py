from django.shortcuts import render
from .models import Book

# Create your views here.

def book_list(request):
    books = Book.objects.all()  # استرجاع جميع الكتب
    context = {'book_list': books}  # إرسال البيانات إلى القالب
    return render(request, 'bookshelf/book_list.html', context)