# relationship_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetail.as_view(), name='LibraryDetail'),
]

