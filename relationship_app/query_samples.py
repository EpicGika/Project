from  relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author


def get_book_by_author(author_name):
    author = Author.objects.get(name=author_name)

    return Book.objects.filter(author=author)


# List all books in a library

def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()


def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)